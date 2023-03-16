from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=254, db_index=True)  # db_index=True to speed up searches
    content = models.CharField(max_length=10_000, help_text="Enter the content of your Post here")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("auth.User", related_name="posts_owner", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_post")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("auth.User", related_name="comments_owner", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.body
