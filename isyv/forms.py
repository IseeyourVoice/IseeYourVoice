from django import forms
from django.forms import ModelForm
from .models import Comment, FileUpload, VoiceLearning, VoiceCreate


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'cut_start', 'cut_end', 'pitch', 'sound_file']


class VoiceLearningForm(ModelForm):
    class Meta:
        model = VoiceLearning
        fields = ['file']


class VoiceCreateForm(ModelForm):
    class Meta:
        model = VoiceCreate
        fields = ['model', 'file']
