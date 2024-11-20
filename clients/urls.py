from django.urls import path
from . import views


app_name = 'clients'

urlpatterns = [
    path('validation', views.validations, name='validation'),
]



