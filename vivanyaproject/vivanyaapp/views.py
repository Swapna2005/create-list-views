# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from .models import LoginModel

# class LoginCreate(CreateView):
    # model=LoginModel
    # fields=['username','Password']
    # template_name='loginmodel_form.html'
from django.views.generic.list import ListView
from .models import LoginModel

class LoginList(ListView):
    model = LoginModel
    template_name = 'Loginmodel_list.html'
    context_object_name='login_list'
