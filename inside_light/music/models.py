from django.db import models

from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    file = models.FileField(upload_to='songs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Testimony(models.Model):
    user_name = models.CharField(max_length=100)
    testimony_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

