from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField(timezone.now())
    views = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    comment = models.TextField()
    image = models.CharField(max_length=200, default='https://pluspng.com/img-png/user-png-icon-account-avatar-human-male-man-men-people-person-download-svg-download-png-edit-icon-512.png',
                             null=True, blank=True)
    commented_at = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.blog.title
