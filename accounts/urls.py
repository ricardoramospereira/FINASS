from django.urls import path
from .import views

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('see_accounts/', views.see_accounts, name='see_acoounts')
]