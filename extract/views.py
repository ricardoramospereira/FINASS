from django.shortcuts import render
from financial.models import Category, Account

# Create your views here.
def new_value(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        categories = Category.objects.all()

        context = {
            "accounts": accounts,
            "categories": categories
        }

        return render(request, 'extract/new_value.html', context)