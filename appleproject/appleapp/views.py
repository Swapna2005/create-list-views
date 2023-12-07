from django.views.generic.edit import  CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import RegisterModel

class RegisterCreate(CreateView):
    model= RegisterModel
    fields= ['Username','Email','Password']
    template_name='register_form.html'
    success_url='/success/'

class RegisterList(ListView):
    model= RegisterModel
    template_name='register_list.html'
    context_object_name='register_list'

class RegisterDetailView(DetailView):
    model= RegisterModel
    template_name= 'register_detail.html'
    context_object_name='register_model'

class RegisterUpdateView(UpdateView):
    model= RegisterModel
    fields=["Username","Email","Password"]
    template_name= 'register_update.html'
    success_url = '/UpdateView/'

class RegisterDeleteView(DeleteView):
    model= RegisterModel
    template_name= 'register_confirm_delete.html'
    success_url= reverse_lazy('register_list')
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['Username']='confirm delete register object'
        return context        