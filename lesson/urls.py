from django.urls import path
from lesson.views import index, categorylist, post_detail, post_delete, CategoryList, CategoryDetail, CategoryCreate, \
    CategoryUpdate

urlpatterns = [
    path('', index, name='index'),
    path('categorylist/', categorylist, name='category_list'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('post_delete/<int:post_id>', post_delete, name='post_delete'),
    path('categorylist_g/', CategoryList.as_view(), name='category_list_g'),
    path('category_detail/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    path('category_create',CategoryCreate.as_view(), name='category_create'),
    path('category_update/<int:pk>',CategoryUpdate.as_view(), name='category_update'),
]