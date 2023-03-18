import random

from blog.models import Comment, Post

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

"""
class Post(models.Model):
    title = models.CharField(max_length=254)
    content = models.CharField(max_length=10_000, help_text="Enter the content of your Post here")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("auth.User", related_name="posts_owner", on_delete=models.CASCADE)

class Comment(models.Model):
    body = models.TextField(help_text="Enter the content of your Comment here")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_post")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("auth.User", related_name="comments_owner", on_delete=models.CASCADE)

"""


class Command(BaseCommand):
    help = "Creating fake 20 Posts, 50 Comments"  # noqa: A003

    def handle(self, *args, **options):
        fake = Faker()
        list_posts = []
        list_comments = []

        # Creating 20 Posts
        postowner_id = User.objects.exclude(is_superuser=1).values_list("id", flat=True)

        for _ in range(20):
            title = fake.text(18)
            content = fake.text(500)
            owner = User.objects.get(pk=random.choice(postowner_id))
            list_posts.append(
                Post(
                    title=title,
                    owner=owner,
                    content=content,
                )
            )

        Post.objects.bulk_create(list_posts)
        posts_id = Post.objects.values_list("id", flat=True)

        # Creating 50 Comments
        for _ in range(50):
            body = fake.text(50)
            post = Post.objects.get(pk=random.choice(posts_id))
            owner = User.objects.get(pk=random.choice(postowner_id))
            list_comments.append(Comment(body=body, post=post, owner=owner))

        Comment.objects.bulk_create(list_comments)

        self.stdout.write(self.style.SUCCESS("Successfully created fake 20 Posts, 50 Comments"))
