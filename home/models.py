from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

   
    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Member, through='Comment')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home_detail', kwargs={'pk': self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.post.title} - {self.member.user.username}'
    
    