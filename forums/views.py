from django.shortcuts import render
from .forms import NewUserCreationForm, ForumForm, PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Forum, Session, Post, Comment


def log_process(request, signup1=False):
    go = False
    if request.user.is_authenticated():
        if request.method == 'POST':
            if 'commenttext' in request.POST:
                if request.POST['commenttext'] == '':
                    messages.error(request, 'You Comment can\'t be nothing')
                return True
            elif 'text' in request.POST:
                if request.POST['text'] == '' and request.POST['title'] == '':
                    messages.error(request, 'Title and text can not be empty')
                elif request.POST['title'] == '':
                    messages.error(request, 'Title can not be empty')
                elif request.POST['text'] == '':
                    messages.error(request, 'Text can not be empty')
                return True
            elif 'name' in request.POST:
                if request.POST['name'] == '':
                    messages.error(request, 'Forum name can\'t not be empty')
                return True
            elif 'logout' in request.POST and request.POST['logout'] == '':
                logout(request)
            else:
                print('Not logout tag')
                messages.error(request, 'No Hacking Please!')
                return True
        else:
            go = True
    else:
        if signup1 == True:
            return False
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                go = True
            else:
                print('Invalid User')
                messages.error(request, 'Invalid User')
    return go


# Create your views here.
def home(request):

    go = log_process(request)
    print(go)

    space = Forum.objects.all()

    forum = ForumForm(request.POST or None)
    if forum.is_valid():
        instance = forum.save(commit=False)
        instance.founder = request.user
        instance.urlname = request.POST['name'].replace(' ', '').replace("'", "").lower()
        default_session_creation = Session()
        instance.save()
        default_session_creation.name = 'k1n234#$normal$%^&*'
        default_session_creation.forum = instance
        default_session_creation.urlname = instance.urlname
        default_session_creation.save()

    posts = Post.objects.all()
    context = {
        'n': range(8),
        'go': go,
        'forum': forum,
        'space': space,
        'posts': posts,
    }
    return render(request, 'base.html', context)


def space(request, name, session="k1n234#$normal$%^&*"):
    try:
        forum = Forum.objects.get(urlname=name)
    except Forum.DoesNotExist:
        messages.error(request, 'Forum does not exist yet, but you can create one.')
        return HttpResponseRedirect('/')

    go = log_process(request)

    sessions = Session.objects.filter(forum=forum)
    if session != "k1n234#$normal$%^&*":
        try:
            mysession = sessions.get(urlname=session)
        except Session.DoesNotExist:
            messages.error(request, 'Your session doesn\'t exist. You can ask your manager to create one.')
            return HttpResponseRedirect('/space/' + name)
    else:
        mysession = sessions.get(name="k1n234#$normal$%^&*")

    postform = PostForm(request.POST or None)

    if postform.is_valid():
        instance = postform.save(commit=False)
        instance.session = mysession
        instance.writer = request.user
        instance.forum = forum
        instance.urlname = request.POST['title'].replace(' ', '').replace("'", "").lower()
        instance.save()

    posts = Post.objects.filter(forum=forum, session=mysession)

    context = {
        'n': range(8),
        'go': go,
        'forum': forum,
        'mysession': mysession,
        'sessions': sessions,
        'postform': postform,
        'posts': posts,
    }
    return render(request, 'space.html', context)


def signup(request):
    go = log_process(request, True)
    if go:
        return HttpResponseRedirect('/')
    else:
        form = NewUserCreationForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Now you have your username:' + str(request.POST['username'])+
                                 '. You can login with it! :D')

    context = {
        'n': range(8),
        'signup': form,
        'go': go,
    }
    return render(request, 'signup.html', context)


def page(request, forum, session, article):
    go = log_process(request)
    myforum = Forum.objects.get(urlname=forum)
    mysession = Session.objects.filter(forum=myforum).get(urlname=session)
    posts = Post.objects.filter(forum=myforum, session=mysession)
    previous = None
    next = None
    for i in range(len(posts)):
        if posts[i].urlname == article:
            mypage = posts[i]
            if i - 1 >= 0:
                next = posts[i - 1]
            if i + 1 < len(posts):
                previous = posts[i + 1]
            break

    commentform = CommentForm(request.POST or None)
    if commentform.is_valid():
        instance = commentform.save(commit=False)
        instance.writer = request.user
        instance.post = mypage
        instance.save()

    comments = Comment.objects.filter(post=mypage)
    context = {
        'go': go,
        'page': mypage,
        'forum': myforum,
        'session': mysession,
        'previous': previous,
        'next': next,
        'form': commentform,
        'comments': comments,
    }
    return render(request, 'page.html', context)
