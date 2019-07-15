from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import (
  LoginView, LogoutView, PasswordResetView, PasswordChangeDoneView, 
  PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
) 

urlpatterns = [
  url(r'^$', views.home),
  url('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
  url('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
  url(r'^register/$', views.register, name='register'),
  url(r'^profile/$', views.view_profile, name='profile'),
  url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
  url(r'^about/$', views.about, name='about'),
  url(r'^profile/password/$', views.pass2),
  url(r'^change_password/$', views.change_password, name='change_password'),
  path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        success_url=reverse_lazy('password_reset_done')
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset_<uidb64>_<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')
    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]