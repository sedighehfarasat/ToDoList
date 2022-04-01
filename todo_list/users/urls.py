from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='users-login'),
    path('logout/', LogoutView.as_view(next_page='users-login'), name='users-logout'),
    path('register/', views.UserRegisterView.as_view(), name='users-register'),
]