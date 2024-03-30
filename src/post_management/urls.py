from django.urls import path, include
from . import api_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'post_management'

post_endpoints = [
    path('get/<int:post_id>/', api_views.getPostByID, name='get_post'),
    path('create/', api_views.createPost, name='create_post'),
    path('update/<int:post_id>/', api_views.updatePost, name='update_post'),
    path('delete/<int:post_id>/', api_views.deletePost, name='delete_post'),
]

token_endpoints = [
    path('get/', TokenObtainPairView.as_view(), name='get_token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token')
]

api_endpoints = [
    path('post/', include(post_endpoints)),
    path('token/', include(token_endpoints)),
]

urlpatterns = [
    path('api/', include(api_endpoints)),
]

