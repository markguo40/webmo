from django.contrib.auth.models import User
from django.forms import EmailField, CharField
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Session, Forum, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['name']


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['name']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commenttext']

class NewUserCreationForm(UserCreationForm):
    email = EmailField(label="Email address", required=True, help_text="Required.")
    first_name = CharField(max_length=41, required=False, label='Your First Name(op)')
    last_name = CharField(max_length=61, required=False, label='Your Last Name(op)')

    class Meta:
        model = User
        fields = ("username", "email", 'first_name', 'last_name', "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data['password1'])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
