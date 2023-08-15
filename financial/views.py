from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Account, Category
from django.contrib.messages import constants
from django.contrib import messages
from django.core.paginator import Paginator, Page


# Create your views here.
def financial_index(request):
    accounts = Account.objects.all()

    paginator = Paginator(accounts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    total_balance = sum(account.value for account in page_obj)

    context = {
         'accounts': accounts,
         'total_balance': total_balance,
         'page_obj': page_obj
    }

    return render(request, 'financial/financial_index.html', context)


def manage_financial(request):
    if request.method == "GET":
        account = Account.objects.all()
        category = Category.objects.all()

        context = {
            "account": account,
            "category": category
        }
    return render(request, 'financial/manage_financial.html', context)


def register_bank(request):
        if request.method == "GET":
            return render(request, 'financial/financial/manage_financial.html')

        elif request.method == "POST":
             bank = request.POST.get('bank')
             type = request.POST.get('type')
             value = request.POST.get('value')

             #TODO: validações

        account = Account(
             bank = bank,
             type = type,
             value = value
        )

        account.save()
        messages.add_message(request, constants.SUCCESS, "Banco cadastrado com sucesso")

        return redirect('/finantial/manage_financial/')
