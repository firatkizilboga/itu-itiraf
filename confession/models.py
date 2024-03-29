from django.db import models
from api.models import User
# Create your models here.

class Post(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=80, default='Anonim')
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null = True, blank = True, upload_to='images/')
    class Meta:
        abstract = True
    def __str__(self):
        return self.title
    
class Confession(Post):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Comment(Post):
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE)
    def __str__(self):
        return '%s - %s' % (self.confession.title, self.body)

class ConfessionIdentityRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'confession')
    def __str__(self):
        return '%s - %s' % (self.user.username, self.confession.title)