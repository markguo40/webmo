from django.contrib import admin
from django.contrib.auth.models import User
from .forms import NewUserCreationForm, ForumForm, SessionForm, PostForm, CommentForm
from .models import Forum, Session, Post, Comment


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    class Meta:
        form = NewUserCreationForm
    list_display = ['username', 'email']


class ForumAdmin(admin.ModelAdmin):
    class Meta:
        form = ForumForm
    list_display = ['name', 'urlname', 'founder', 'date']


class SessionAdmin(admin.ModelAdmin):
    class Meta:
        form = SessionForm
    list_display = ['name', 'urlname', 'forum', 'date']


class PostAdmin(admin.ModelAdmin):
    class Meta:
        form = PostForm
    list_display = ['title', 'session', 'forum', 'writer', 'date']


class CommentAdmin(admin.ModelAdmin):
    class Meta:
        form = CommentForm
    list_display = ['writer', 'date', 'post']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)