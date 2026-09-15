from django.urls import path
from . import views

app_name = 'apprama2'

urlpatterns = [
    path('vista1/', views.vista1_apprama2, name='vista1_apprama2'),
    path('vista2/', views.vista2_apprama2, name='vista2_apprama2'),
]