from django.urls import path
from .import views

urlpatterns = [
    path('new_value/', views.new_value, name='new_value')
]