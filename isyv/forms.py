from django import forms
from django.forms import ModelForm
from .models import Comment, FileUpload


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'cut_start', 'cut_end', 'pitch', 'sound_file']
