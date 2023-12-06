

# from django.shortcuts import render
# from .models import ForgettModel
# from django.views.generic.edit import CreateView

# class ForgettCreate(CreateView):
#     model=ForgettModel
#     fields=['Email','phone','Password']
#     template_name='forgett_form.html'

from django.views.generic.list import ListView
from .models import ForgettModel

class ForgettList(ListView):
    model = ForgettModel
    template_name = 'Forgettmodel_list.html'
    context_object_name='login_list'