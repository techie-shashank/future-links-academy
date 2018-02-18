from django import forms
from .models import Test,Question

class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = ['title','subject']

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields=['question','option1','option2','option3','right_answer']
 