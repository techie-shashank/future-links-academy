from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Test,Question,Score
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .forms import TestForm, QuestionForm
from django.views.generic.base import TemplateView



class TestList(generic.ListView):

	def get_queryset(self):
		queryset = Test.objects.all()
		return queryset

class TestPaperView(generic.DetailView):
	template_name='tests/test_detail.html'
	model = Test

	def post(self, request, *args, **kwargs):
		slug = self.kwargs.get("slug")
		this = Test.objects.get(slug=slug)
		score = 0
		wrong_answers = []
		for ques in this.question_set.all():
			if ques.right_answer == self.request.POST[str(ques.id)]:
				score= score + 1
			else:
				wrong_answers.append(ques.question_no)
		created,result = Score.objects.get_or_create(test=this,marks=score,user=request.user)
		if created:
			return HttpResponse("You've already submitted the test")	
		string = " ".join(str(x) for x in wrong_answers)
		result.wrong_questions = string
		result.save()
		return render(request,'tests/result.html',{
			'score' : score,
			'wrong_answers': wrong_answers,
			})

class AddTestView(generic.CreateView):
	form_class = TestForm
	login_url = "/login/"
	template_name = 'tests/add_test_form.html'

	def get_success_url(self):
		return reverse('tests:testpaper', kwargs={'slug': self.object.slug})

	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(AddTestView,self).form_valid(form)

class AddQuestionView(generic.CreateView):
	form_class = QuestionForm
	login_url = "/login/"
	template_name = 'tests/add_question_form.html'

	def get_success_url(self,*args,**kwargs):
		return reverse('tests:testpaper', kwargs={'slug': self.kwargs['slug']})

	def form_valid(self,form,*args,**kwargs):
		instance = form.save(commit=False)
		test = get_object_or_404(Test, slug=self.kwargs['slug'])
		instance.test = test
		return super(AddQuestionView,self).form_valid(form)
	

class AboutView(TemplateView):
	template_name = "about.html"

class Marksheet(generic.DetailView):
	template_name='tests/marksheet.html'
	model = Test

	def get_context_data(self,*args,**kwargs):
		context = super(Marksheet,self).get_context_data(*args,**kwargs)
		return context






