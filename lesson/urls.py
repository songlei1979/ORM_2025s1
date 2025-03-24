from django.urls import path
from lesson.views import index, categorylist

urlpatterns = [
    path('', index, name='index'),
    path('categorylist/', categorylist, name='category_list'),
]