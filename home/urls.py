from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:url>/', views.renderizator, name='renderizator'),
]
