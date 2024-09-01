from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('prices/', views.PricesView.as_view(), name='prices'),
]