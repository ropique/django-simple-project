from django.contrib import admin
from django.urls import path, include 
from users import views as user_views 
from django.contrib.auth import views as auth_views 
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name = "users/login.html"), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name = "users/logout.html"), name='logout'), 
    path('profile/', user_views.profile, name='profile'), 
    path('post/', views.PostList),
    path('post/<int:id>', views.post_detail)
    




]
urlpatterns = format_suffix_patterns(urlpatterns)