from django.urls import path
from .views import RegisterCreate,RegisterList,RegisterDetailView,RegisterUpdateView,RegisterDeleteView

urlpatterns = [
    path('Register/Create/',RegisterCreate.as_view(),name='register_create'),
    path('Register/List/',RegisterList.as_view(),name='register_list'),
    path('Register/Detail/<int:pk>/',RegisterDetailView.as_view(),name='login_detailview'),
    path('Register/Update/<int:pk>/',RegisterUpdateView.as_view(),name='register_updateview'),
    path('Register/Delete/<int:pk>/',RegisterDeleteView.as_view(),name='register_deleteview'),



]