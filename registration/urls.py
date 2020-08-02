from django.urls import path, include
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(form_class=CustomAuthenticationForm), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
