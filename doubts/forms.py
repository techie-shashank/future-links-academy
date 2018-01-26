from django import forms
from .models import Question, Answers


class AskQuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = [
			'content',
		]

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answers
		fields = [
			'text',
		]

