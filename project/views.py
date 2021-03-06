
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

class IndexView(generic.TemplateView):
    
    template_name ='index.html'

    def get(self, request):
        if(request.user.is_authenticated):
            return render(request, 'index.html')
        else:
            return redirect('/login')
