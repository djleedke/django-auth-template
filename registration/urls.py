from django.urls import path, include
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(form_class=CustomAuthenticationForm), name='login'),
    path('signup/', views.SignUpView.as_view(form_class=CustomUserCreationForm), name='signup'),
]
