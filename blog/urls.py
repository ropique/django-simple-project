from django.urls import path
from .import views
from .views import  PostDetailView,  PostListView, PostCreateView

urlpatterns = [
    
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/add_post/', PostCreateView.as_view(), name='add_post'),
]