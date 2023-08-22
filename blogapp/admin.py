from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register the Post model with SummernoteModelAdmin for rich text editing
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    # Automatically populate the slug based on the title
    prepopulated_fields = {'slug': ('title',)}
    # Enable Summernote rich text editing for the 'content' field
    summernote_fields = ('content',)


# Register the Comment model with a regular admin.ModelAdmin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    # Custom action to approve selected comments
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
