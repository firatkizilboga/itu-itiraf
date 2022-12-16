from django.db import models

# Create your models here.

class Confession(models.Model):
    title = models.CharField(max_length=100, null=False)
    body = models.TextField(default=title)
    author = models.CharField(max_length=80, default='Anonim')
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80,default='Anonim')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.confession.title, self.name)