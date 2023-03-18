from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=254)
    content = models.CharField(max_length=10_000, help_text="Enter the content of your Post here")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("auth.User", related_name="posts_owner", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Post -> P-ID: {self.id}|P-Title: {self.title}|P-Author: {self.owner}"


class Comment(models.Model):
    body = models.TextField(help_text="Enter the content of your Comment here")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_post")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("auth.User", related_name="comments_owner", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment -> C-ID: {self.id}| C-Body: {self.body}|C-Author: {self.owner}|C-Post {self.post}"
