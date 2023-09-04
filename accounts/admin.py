from django.contrib import admin
from .models import Bill_to_pay

# Register your models here.
@admin.register(Bill_to_pay)
class Bill_to_payAdmin(admin.ModelAdmin):
    list_display = ("title",)