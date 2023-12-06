# from django.shortcuts import render
# from .models import RegisterModel
# from django.views.generic.edit import CreateView

# class RegisterCreate(CreateView):
#     model=RegisterModel
#     fields=['username','Email','Password']
#     template_name='register_form.html'


from django.views.generic.list import ListView
from .models import RegisterModel

class LoginList(ListView):
    model = RegisterModel
    template_name = 'registermodel_list.html'
    context_object_name='login_list'