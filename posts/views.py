import random

from django.shortcuts import render, HttpResponse

from posts.models import Post


def test_view(request):
    return HttpResponse(f"Hello World {random.randint(1, 100)}")


def cookies_view(request):
    return HttpResponse('Cookies')


def html_view(request):
    return render(request, "main.html")


def video(request):
    return render(request, "video.html")


def post_list_view(request):
    posts = Post.objects.all()
    print(posts)
    for post in posts:
        print(post.title)
    return render(request, 'posts/post_list.html', context={'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', context={'post': post})