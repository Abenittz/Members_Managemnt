# models.py
from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields for members if needed

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Member, through='Comment')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.post.title} - {self.member.user.username}'
