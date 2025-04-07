from django.urls import path
from lesson.views import index, categorylist, post_detail, post_delete, CategoryList, CategoryDetail, CategoryCreate, \
    CategoryUpdate, CategoryDelete, like_post, ProfileDetail, ProfileCreate, ProfileUpdate

urlpatterns = [
    path('', index, name='index'),
    path('categorylist/', categorylist, name='category_list'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('post_delete/<int:post_id>', post_delete, name='post_delete'),
    path('categorylist_g/', CategoryList.as_view(), name='category_list_g'),
    path('category_detail/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    path('category_create',CategoryCreate.as_view(), name='category_create'),
    path('category_update/<int:pk>',CategoryUpdate.as_view(), name='category_update'),
    path('category_delete/<int:pk>',CategoryDelete.as_view(), name='category_delete'),
    path('like_post/<int:post_id>', like_post, name='like_post'),
    path('profile/', ProfileDetail.as_view(), name='profile_detail'),
    path('create_profile/', ProfileCreate.as_view(), name='create_profile'),
    path('update_profile/<int:pk>', ProfileUpdate.as_view(), name='update_profile'),
]