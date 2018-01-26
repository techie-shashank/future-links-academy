from django import forms
from .models import Test,Question

class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = ['title']

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields=['question_no','question','option1','option2','option3','option4','right_answer']
