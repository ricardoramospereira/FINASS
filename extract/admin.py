from django.contrib import admin
from.models import Values

# Register your models here.
@admin.register(Values)
class ValuesAdmin(admin.ModelAdmin):
    list_display = ("description",)