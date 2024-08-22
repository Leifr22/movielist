from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from . import views
from django.urls import path

from .views import RegisterView, ProfileUser

urlpatterns = [
    path('login/',views.LoginUser.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/', ProfileUser.as_view(),name='profile'),
    path('password-change/',views.UserPasswordChange.as_view(),name='password_change'),
    path('password-change/done',PasswordChangeDoneView.as_view(template_name="user/password_change_done.html"),name='password_change_done'),
    path('password-reset-form/',PasswordResetView.as_view(template_name='user/password_reset_form.html'),name='password_reset_form'),
    path('password-reset-form/done/',PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-confirm/complete/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete')
]