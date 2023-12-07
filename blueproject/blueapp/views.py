from typing import Any
from django.views.generic.edit import  CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import LoginModel

class LoginCreate(CreateView):
    model= LoginModel
    fields= ['Username','Password']
    template_name='login_form.html'
    success_url='/success/'

class LoginList(ListView):
    model= LoginModel
    template_name='login_list.html'
    context_object_name='login_list'


class LoginDetailView(DetailView):
    model= LoginModel
    template_name= 'login_detail.html'
    context_object_name='login_model'


class LoginUpdateView(UpdateView):
    model= LoginModel
    fields=["Username","Password"]
    template_name= 'login_update.html'
    success_url = '/UpdateView/'

class LoginDeleteView(DeleteView):
    model= LoginModel
    template_name= 'login_confirm_delete.html'
    success_url= reverse_lazy('login_list')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['Username']='confirm delete login object'
        return context
       
