from django.urls import path
from .views import RegisterView, UserDetailUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserDetailUpdateView.as_view(), name='edit-profile'),
]

from django.urls import path
from .views import custom_logout_view, CustomLoginView, register_view, reset_password_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('reset-password/', reset_password_view, name='reset_password')
]
