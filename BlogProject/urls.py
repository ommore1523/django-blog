

from django.contrib import admin
from django.urls import path,include

#from user app render a register view function
from users import views as user_view

#inbuilt login and logout 
from django.contrib.auth import views as auth_views

#library for image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('blog/',include('blogapp.urls')),

    #user app function render
    path('register/',user_view.register,name='register'),
    path('profile/',user_view.profile,name='profile'),

    #inbuilt login and logout 
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view() ,name="logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html") ,name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html") ,name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html") ,name="password_reset_confirm"),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html") ,name="password_reset_complete")

    
    

] 

# image profile
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
