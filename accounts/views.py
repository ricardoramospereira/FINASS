from django.shortcuts import render
from financial.models import Category

# Create your views here.
def accounts(request):
    if request.method == "GET":
        categories = Category.objects.all()

        context = {
            'categories': categories
        }

        return render(request, 'accounts/accounts.html', context)