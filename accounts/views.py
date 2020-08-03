from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import User
from .forms import UserSettingsForm


class CustomLoginView(LoginView):

    #If a user is already logged in we redirect to index
    def get(self, request):
        if(request.user.is_authenticated):
            return redirect('/')
        else:
            return super().get(request)

class UserSettingsView(generic.UpdateView):
    
    model = User
    form_class = UserSettingsForm
    template_name = 'accounts/settings.html'
    success_url = '/settings'

    def form_valid(self, form):
        messages.success(self.request, 'Updated!')
        return super(UserSettingsView, self).form_valid(form)


    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

class SignUpView(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def get(self, request):
        if(request.user.is_authenticated):
            return redirect('/')
        else:
            return render(request, self.template_name, {'form' : self.form_class})

            