from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ajax/get_prices/', views.getPrices, name='get_prices'),
]