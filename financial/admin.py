from django.contrib import admin
from .models import Category, Account

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "essential")
    list_editable = ("essential",)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("bank", "type", "value")