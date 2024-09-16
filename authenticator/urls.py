from django.urls import path
from .views import UserLoginView, UserRegister
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', UserRegister.as_view(), name='register'),
]