from django.urls import path
from lesson.views import index, categorylist, post_detail, post_delete

urlpatterns = [
    path('', index, name='index'),
    path('categorylist/', categorylist, name='category_list'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('post_delete/<int:post_id>', post_delete, name='post_delete')
]