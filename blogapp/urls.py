from . import views
from django.urls import path,include

from .views import (PostListview ,
                    PostDetailView ,
                    PostCreateview,
                    PostUpdateview ,
                    PostDeleteview,
                    UserPostListview )


urlpatterns = [
     # path('', views.home, name='home'),
     path('', PostListview.as_view(), name='home'),
     path('user/<str:username>/', UserPostListview.as_view(), name='user_posts'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
     path('post/new/', PostCreateview.as_view(), name='post_create'),
     path('post/<int:pk>/update/', PostUpdateview.as_view(), name='post_update'),
     path('post/<int:pk>/delete/', PostDeleteview.as_view(), name='post_delete'),
     path('about/', views.about, name='about'),
     
]