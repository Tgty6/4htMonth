import random

from django.shortcuts import render, HttpResponse, redirect

from posts.models import Post

from posts.forms import PostCreateForm
from django.contrib.auth.decorators import login_required


def test_view():
    return HttpResponse(f"Hello World {random.randint(1, 100)}")


def cookies_view(request):
    return HttpResponse('Cookies')


def html_view(request):
    return render(request, "main.html")


def video(request):
    return render(request, "video.html")

@login_required(login_url='/login/')
def post_list_view(request):
    posts = Post.objects.all()
    print(posts)
    for post in posts:
        print(post.title)
    return render(request, 'posts/post_list.html', context={'posts': posts})

@login_required(login_url='/login/')
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', context={'post': post})

@login_required(login_url='/login/')
def post_create_view(request):
    global post
    if request.method == "GET":
        form = PostCreateForm
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        elif form.is_valid():
            image = form.cleaned_data.get('image')
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            post = Post.objects.create(image=image, title=title, content=content)
        if post:
            return redirect('/posts/')
        else:
            return  HttpResponse("Пост не был создан")