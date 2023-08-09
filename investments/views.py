from django.shortcuts import render
from .models import Investment

# Create your views here.
def investment(request):
    if request.method == "GET":
        investment = Investment.objects.all()
        
        context = {
            "investment": investment
        }


        return render(request, 'investments/investment.html', context)
    
    elif request.method == "POST":
        pass


def new_investment(request):
    return render(request, 'investiments/new_investment.html')


def detail_investment(request, id):
    detail = Investment.objects.get(id=id)

    context = {
        "detail": detail
    }

    return render(request, 'investments/detail_investment.html', context)