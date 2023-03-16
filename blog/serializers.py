from blog.models import Comment, Post

from django.contrib.auth.models import User

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_on", "updated_on", "owner", "comments_post"]

    owner = serializers.ReadOnlyField(source="owner.username")
    comments_post = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "body", "post", "created_on", "updated_on", "owner"]

    owner = serializers.ReadOnlyField(source="owner.username")


class UserSerializer(serializers.ModelSerializer):
    posts_owner = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    comments_owner = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "posts_owner", "comments_owner"]
