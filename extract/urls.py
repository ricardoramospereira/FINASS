from django.urls import path
from .import views

urlpatterns = [
    path('new_value/', views.new_value, name='new_value'),
    path('view_extract/', views.view_extract, name='view_extract'),
    #path('export_extract/', views.export_extract, name='export_extract'),
]