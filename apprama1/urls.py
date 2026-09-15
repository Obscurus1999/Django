from django.urls import path
from . import views

app_name = 'apprama1'

urlpatterns = [
    path('vista1/', views.vista1_apprama1, name='vista1_apprama1'),
    path('vista2/', views.vista2_apprama1, name='vista2_apprama1'),
]