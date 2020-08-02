from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def get(self, request):
        if(request.user.is_authenticated):
            return redirect('/')
        else:
            return render(request, self.template_name, {'form' : self.form_class})