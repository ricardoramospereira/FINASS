from django.contrib import admin
from .models import Investment

# Register your models here.
@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ("name","value","status")
    list_editable = ("status",)
    list_per_page = 10