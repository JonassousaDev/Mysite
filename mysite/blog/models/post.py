from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)
    object = models.Manager()

    class Meta:
        ordering = ['-created_on']  #decrescent


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['created_on']  #ascending

    def __str__(self):
        return self.content


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


