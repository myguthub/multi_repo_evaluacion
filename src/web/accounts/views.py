from django.shortcuts import render

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class AccRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/cr-acc.html'
    success_url = reverse_lazy('home.html')

# Create your views here.
