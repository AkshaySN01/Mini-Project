from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    Email_Ph_no=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='profile_pic/')
    is_staff = models.BooleanField(default=True)

class Posts(models.Model):
    username=models.ForeignKey(Users, on_delete=models.CASCADE)
    caption=models.CharField(max_length=500)
    photo=models.ImageField(upload_to='photos/')
    likes=models.ManyToManyField(Users, related_name='post_likes')

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)