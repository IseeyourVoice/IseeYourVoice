from django.db import models
from config import settings

class Audio(models.Model):
    title = models.CharField(max_length=100)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audios/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)


class EditedAudio(models.Model):
    original_audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    edited_audio_file = models.FileField(upload_to='edited_audios/')
    edited_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)


class FileUpload(models.Model):
    title = models.CharField(max_length=20, null=True)
    cut_start = models.IntegerField(null=True)
    cut_end = models.IntegerField(null=True)
    pitch = models.IntegerField(null=True)
    sound_file = models.FileField(null=True, upload_to="", blank=True)

    def __str__(self):
        return self.title


class VoiceLearning(models.Model):
    file = models.FileField(null=True, upload_to="", blank=True)


class VoiceCreate(models.Model):
    model = models.FileField(null=True, upload_to="", blank=True)
    file = models.FileField(null=True, upload_to="", blank=True)
