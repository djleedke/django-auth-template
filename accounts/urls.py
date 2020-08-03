from django.urls import path, include
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(form_class=CustomAuthenticationForm), name='login'),
    path('signup/', views.SignUpView.as_view(form_class=CustomUserCreationForm), name='signup'),
    #path('settings/<int:pk>/', views.UserSettingsView.as_view(), name='settings')
    path('settings/', views.UserSettingsView.as_view(), name='settings')
]
