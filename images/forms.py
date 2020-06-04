from django import forms
from .models import Profile, Image, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'likes', 'date_posted',  'comment', 'profile']

class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']