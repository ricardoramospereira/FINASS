from django.urls import path
from .import views

urlpatterns = [
    path('', views.investment, name='investment'),
    path('new_investment', views.new_investment, name='new_investment'),
]