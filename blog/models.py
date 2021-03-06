from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, on_delete=models.CASCADE) #IF user is deleted then all posts will be deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):#after create it will retun reverse to detial of that post
        return reverse('post-detail', kwargs={'pk': self.pk})
