from django import forms
from django.forms import Textarea
from .models import Question, Answers


class AskQuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = [
			'content',
		]

class AnswerForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':"Write your question here...",}), label='',)
	class Meta:
		model = Answers
		fields = [ 'text',]

