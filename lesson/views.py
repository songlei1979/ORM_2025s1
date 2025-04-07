from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from lesson.forms import CreateCategoryForm
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


class CategoryList(ListView):
    template_name = 'categorylist_g.html'
    model = Category


class CategoryCreate(CreateView):
    model = Category
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list_g')
    form_class = CreateCategoryForm


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category_update.html'
    success_url = reverse_lazy('category_list_g')


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list_g')


class CategoryDetail(DetailView):
    template_name = 'category_detail.html'
    model = Category


def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return render(request, 'post_detail.html',
                  {'post': post})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if password == password2:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            first_name=first_name,
                                            last_name=last_name)
            user.set_password(password)
            user.save()
            return redirect('login')
    return render(request, 'register.html')
