from django.urls import path
from .import views

urlpatterns = [
    path('', views.financial_index, name='financial_index'),
    path('manage_financial/', views.manage_financial, name='manage_financial')
]