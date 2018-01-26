from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddPostCreateForm, CommentForm
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class BlogHome(generic.ListView):

	def get_queryset(self,*args,**kwargs):
		queryset = Post.objects.order_by("timestamp")[:2]
		return queryset

	def get_context_data(self, *args,**kwargs):
		context = super(BlogHome,self).get_context_data(*args,**kwargs)
		array = Post.objects.values('category').distinct()
		context['array'] = array
		popular = Post.objects.order_by("-likes")[:2]
		context['popular'] = popular
		return context

	def post(self,request):
		queryset = Post.objects.filter(title__icontains 
			= request.POST['searchbox'])
		return render(request,'blog/post_list.html',{ 'object_list':queryset,'user': request.user })


class PostDetail(FormMixin,generic.DetailView):
	template_name='blog/post_detail.html'
	model = Post
	form_class = CommentForm

	def get_success_url(self):
		return reverse('blog:postdetail', kwargs={'slug': self.object.slug})

	def get_context_data(self, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
		print(context)
		context['form'] = CommentForm(initial={'post': self.object})
		post = get_object_or_404(Post, slug= self.object.slug)
		if post.likes.filter(id=self.request.user.id).exists():
			context['name'] = "Unlike"
		else:
			context['name'] = "Like"
		print(context['name'])
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form,*args,**kwargs):
		instance = form.save(commit=False)
		instance.post = self.object
		form.save()
		return super(PostDetail, self).form_valid(form)

class AddPostCreateFormView(LoginRequiredMixin,generic.CreateView):
	form_class = AddPostCreateForm
	login_url = "/login/"
	template_name = 'blog/form.html'
	success_url = "/blog/"

	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(AddPostCreateFormView,self).form_valid(form)

@login_required
def like(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug')
        post = get_object_or_404(Post, slug=slug)
        check = False
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            name = 'Like'
        else:
            post.likes.add(user)
            name = 'Unlike'
    ctx = {'likes_count': post.total_likes, 'name':name,}
    return JsonResponse(ctx)

def category_list_view(request,category):
	queryset = Post.objects.filter(category__icontains= category)
	return render(request,"blog/category_list.html",{'object_list': queryset})

class PostUpdate(UpdateView):
    model = Post
    fields = ['description']
    template_name_suffix = '_update_form'

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:bloghome')