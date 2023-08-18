from django.shortcuts import render, redirect
from financial.models import Category, Account
from .models import Values
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, timedelta

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
    elif request.method == "POST":
        value = request.POST.get('value')
        category = request.POST.get('category')
        description = request.POST.get('description')
        date = request.POST.get('date')
        account = request.POST.get('account')
        type = request.POST.get('type')

        #TODO: Validations

        values = Values(
            value=value,
            category_id=category,
            description=description,
            date=date,
            account_id=account,
            type=type
        )

        values.save()

        account = Account.objects.get(id=account)

        if type == 'E':
            account.value += int(value)
        else:
            account.value -= int(value)

        account.save()

        if type == 'E':
            messages.add_message(request, constants.SUCCESS, 'Entrada cadastrada com sucesso')
        else:
            messages.add_message(request, constants.SUCCESS, 'Saída cadastrada com sucesso')
        return redirect('/extract/new_value')
    
def view_extract(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        categories = Category.objects.all()
        account_get = request.GET.get('account')
        category_get = request.GET.get('category')
        selected_month = request.GET.get('month', datetime.now().month)  # Obtém o mês selecionado do formulário

        # período selecionado pelo usuário
        selected_period = int(request.GET.get('periodo', 30))  # Padrão para 30 dias
        start_date = datetime.now() - timedelta(days=selected_period)
        values = Values.objects.filter(date__month=selected_month)

        if account_get:
            values = values.filter(account__id=account_get)

        if category_get:
            values = values.filter(category__id=category_get)

        if 'clear_filters' in request.GET:
            values = Values.objects.all()  # Recarrega todos os valores sem filtros

        context = {
            'accounts': accounts,
            'categories': categories,
            'values': values,
            'selected_month': int(selected_month),  # Passa o mês selecionado para o contexto
            'selected_period': selected_period,
        }
        return render(request, 'extract/view_extract.html', context)
    
