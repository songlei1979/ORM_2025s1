from django.shortcuts import render

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
