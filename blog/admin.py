from django.contrib import admin

from .models import Comment, Post


# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "owner",
        "created_on",
        "updated_on",
    )
    list_filter = (
        "owner",
        "created_on",
        "updated_on",
    )
    search_fields = (
        "id",
        "title",
        "created_on",
        "updated_on",
    )
    list_display_links = (
        "id",
        "title",
        "owner",
        "created_on",
        "updated_on",
    )
    list_per_page = 5
    ordering = ["-id"]
    save_as = True

    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "post",
        "created_on",
        "owner",
        "body",
    )
    date_hierarchy = "created_on"
    list_filter = (
        "post",
        "created_on",
    )
    search_fields = (
        "id",
        "post",
        "created_on",
    )
    list_display_links = (
        "id",
        "post",
        "created_on",
    )
    ordering = ["-created_on"]
    save_as = True
    list_per_page = 5
