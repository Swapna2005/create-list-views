from django.urls import path
from .views import LoginCreate,LoginList,LoginDetailView,LoginUpdateView,LoginDeleteView

urlpatterns = [
    path('Login/Create/',LoginCreate.as_view(),name='login_create'),
    path('Login/List/',LoginList.as_view(),name='login_list'),
    path('Login/Detail/<int:pk>/',LoginDetailView.as_view(),name='login_detailview'),
    path('Login/Update/<int:pk>/',LoginUpdateView.as_view(),name='login_updateview'),
    path('Login/Delete/<int:pk>/',LoginDeleteView.as_view(),name='login_deleteview'),


]