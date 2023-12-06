from django.urls import path
# from .views import ForgettCreate
from .views import ForgettList
urlpatterns = [
    #    path('',ForgettCreate.as_view()),
    path('',ForgettList.as_view())
]