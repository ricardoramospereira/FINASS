from django.urls import path
from .import views

urlpatterns = [
    path('', views.financial_index, name='financial_index'),
    path('manage_financial/', views.manage_financial, name='manage_financial'),
    path('register_bank/', views.register_bank, name='register_bank'),
    path('delete_bank/<int:id>', views.delete_bank, name='delete_bank'),
    path('register category/', views.register_category, name='register_category'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    path('update_category/<int:id>', views.update_category, name='update_category'),
]