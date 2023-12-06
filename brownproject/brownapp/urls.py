from django.urls import path
# from .views import RegisterCreate
from .views import LoginList
urlpatterns = [
    #    path('',RegisterCreate.as_view()),
    path('',LoginList.as_view())
]