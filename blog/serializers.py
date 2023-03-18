from blog.models import Comment, Post

from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts_owner = serializers.HyperlinkedRelatedField(many=True, view_name="post-detail", read_only=True)
    comments_owner = serializers.HyperlinkedRelatedField(many=True, view_name="comment-detail", read_only=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "posts_owner", "comments_owner"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    comments_post = serializers.HyperlinkedRelatedField(many=True, view_name="comment-detail", read_only=True)

    class Meta:
        model = Post
        fields = ["url", "id", "title", "content", "created_on", "updated_on", "owner", "comments_post"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Comment
        fields = ["url", "id", "body", "post", "created_on", "updated_on", "owner"]
