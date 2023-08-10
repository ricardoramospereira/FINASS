from django.shortcuts import render, redirect
from .models import Investment
from .forms import InvestmentForm
from django.contrib import messages
from django.contrib.messages import constants

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
    if request.method == "POST":
        investment_form = InvestmentForm(request.POST) 
        if investment_form.is_valid():
            investment_form.save()
            messages.add_message(request, constants.SUCCESS, "Investimento cadastrado com sucesso.")
        return redirect('investment')
    
    else:
        investment_form = InvestmentForm()
        form = {
            'form': investment_form
        }
        return render(request, 'investments/new_investment.html', context=form)


def detail_investment(request, id):
    detail = Investment.objects.get(id=id)

    context = {
        "detail": detail
    }

    return render(request, 'investments/detail_investment.html', context)

def edit(request, id):
    investment = Investment.objects.get(id=id)

    if request.method == "GET":
        form = InvestmentForm(instance=investment)
        return render(request, 'investments/new_investment.html', {'form': form})

    else:
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Investimento atualizado com sucesso')
        return redirect('investment')

def delete(request, id):
    investment = Investment.objects.get(id=id)
    investment.delete()
    messages.add_message(request, constants.SUCCESS, 'Investimento excluido com sucesso')
    return redirect('investment')

        
    