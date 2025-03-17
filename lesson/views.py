from django.shortcuts import render

from lesson.models import Post


# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
    posts = Post.objects.all()
    return render(request,
                  'index.html',
                  {'posts': posts})
