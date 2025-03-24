from django.shortcuts import render
from django.urls import reverse_lazy

from lesson.models import Post, Category


# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        auther_id = request.POST['auther_id']
        Post.objects.create(title=title, content=content, author_id=auther_id)
    posts = Post.objects.all()
    return render(request,
                  'index.html',
                  {'posts': posts})


def categorylist(request):
    categories = Category.objects.all()
    return render(request,
                  'categorylist.html',
                  {'categories': categories})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post.title = title
        post.content = content
        post.save()
    return render(request, 'post_detail.html',
                  {'post': post})

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    posts = Post.objects.all()
    return render(request,
                  'index.html',
                  {'posts': posts})