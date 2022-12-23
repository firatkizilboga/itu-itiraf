from django.db import models
from api.models import User
# Create your models here.

class Confession(models.Model):
    title = models.CharField(max_length=100, null=False)
    body = models.TextField()
    author = models.CharField(max_length=80, default='Anonim')
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE)
    author = models.CharField(max_length=80,default='Anonim')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.confession.title, self.body)