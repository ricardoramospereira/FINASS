from django.contrib import admin
from .models import Bill_to_pay, PaidBills

# Register your models here.
@admin.register(Bill_to_pay)
class Bill_to_payAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(PaidBills)
class Bill_to_payAdmin(admin.ModelAdmin):
    list_display = ("account", "date_bill")