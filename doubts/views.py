from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Question,Answers
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AskQuestionForm, AnswerForm
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.


class DoubtsHome(generic.ListView):

	def get_queryset(self):
		return Question.objects.order_by("timestamp")[:2]

	def get_context_data(self,*args,**kwargs):
		context = super(DoubtsHome,self).get_context_data(*args,**kwargs)
		popular = Question.objects.order_by("-votes")[:2]
		context['popular'] = popular
		return context

 

class QuestionDetail(FormMixin,generic.DetailView):
	template_name='doubts/question_detail.html'
	model = Question
	form_class = AnswerForm

	def get_success_url(self):
		return reverse('doubts:Questiondetail', kwargs={'slug': self.object.slug})

	def get_context_data(self, **kwargs):
		context = super(QuestionDetail, self).get_context_data(**kwargs)
		print(context)
		context['form'] = AnswerForm(initial={'question': self.object})
		array = []
		if self.object.votes.filter(id=self.object.id).exists():
			context['question_vote'] = "Downvote"
		else:
			context['question_vote'] = "Upvote"
		ordered_answers = self.object.answers_set.order_by("-upvotes")
		for ans in ordered_answers:
			if ans.upvotes.filter(id=self.request.user.id).exists():
				array.append("Downvote")
			else:
				array.append("Upvote")
		myarray = zip(ordered_answers,array)
		context['array'] = myarray
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
		instance.question = self.object
		instance.answered_by = self.request.user
		form.save()
		return super(QuestionDetail, self).form_valid(form)

class AskQuestionFormView(LoginRequiredMixin,generic.CreateView):
	form_class = AskQuestionForm
	login_url = "/login/"
	template_name = 'doubts/form.html'
	success_url = "/doubts/"

	def form_valid(self,form):
		form.save()
		return super(AskQuestionFormView,self).form_valid(form)

@login_required
def upvote(request):
    if request.method == 'POST':
        user = request.user
        pk = request.POST.get('pk')
        answer = get_object_or_404(Answers, id= pk )
        print(answer)
        if answer.upvotes.filter(id=user.id).exists():
            answer.upvotes.remove(user)
            name = 'Upvote'
        else:
            answer.upvotes.add(user)
            name = 'Downvote'
    ctx = {'upvotes_count': answer.total_upvotes, 'name':name,}
    return JsonResponse(ctx)

@login_required
def vote(request):
    if request.method == 'POST':
        user = request.user
        pk = request.POST.get('pk')
        question = get_object_or_404(Question, id= pk )
        if question.votes.filter(id=user.id).exists():
            question.votes.remove(user)
            name = 'Upvote'
        else:
            question.votes.add(user)
            name = 'Downvote'
    ctx = {'upvotes_count': question.total_votes, 'name':name,}
    return JsonResponse(ctx)

