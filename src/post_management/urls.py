from django.urls import path, include
from . import api_views

app_name = 'post_management'

post_endpoints = [
    path('get/<int:post_id>/', api_views.getPostByID),
    path('create/', api_views.createPost),
    path('update/<int:post_id>/', api_views.updatePost),
    path('delete/<int:post_id>/', api_views.deletePost),
]

api_endpoints = [
    path('post/', include(post_endpoints)),
]

urlpatterns = [
    path('api/', include(api_endpoints)),
]

