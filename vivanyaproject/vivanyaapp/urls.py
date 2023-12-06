from django.urls import path
# from .views import LoginCreate
from .views import LoginList
urlpatterns = [
    # path('',LoginCreate.as_view()),
    path('',LoginList.as_view()),
]