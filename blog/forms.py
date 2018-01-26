from django import forms
from .models import Post,Comments
from .validators import validate_by
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddPostCreateForm(forms.ModelForm):
	by = forms.CharField(validators=[validate_by])
	class Meta:
		model = Post
		fields = [
			'title',
			'category',
			'by',
			'description',
		]

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ( 'text', )

class UserCreateForm(UserCreationForm):
    occupation=forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "occupation", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.occupation = self.cleaned_data["occupation"]
        if commit:
            user.save()
        return user














	# def clean_title(self):
	# 	title = self.cleaned_data.get("title")
	# 	if title == "hello":
	# 		print(title)
	# 		raise forms.ValidationError("Not a valid Name")
	# 	return title

