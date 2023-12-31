from django.shortcuts import render, redirect
from financial.models import Category, Account
from .models import Values
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, timedelta 
'''import os
from django.template.loader import render_to_string
from django.conf import settings
from weasyprint import HTML
from io import BytesIO #Salve in memory
from django.http import FileResponse'''

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
        if(len(value.strip()) == 0) or (len(category.strip()) == 0) or (len(description.strip()) == 0) or (len(account.strip()) == 0) or (len(date.strip()) == 0) or (len(type.strip()) == 0):
            messages.add_message(request, constants.ERROR, "Preencha todos os campos")
            return redirect('/extract/new_value')

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
        day_range = request.GET.get('day_range') # Obtém o intervalo de dias selecionado do formulário

        # Converta a string para um número inteiro (por padrão, os valores GET são strings)
        if day_range:
            day_range = int(day_range)
     
        values = Values.objects.filter(date__month=selected_month)

         # Se day_range estiver definido, use-o para filtrar os registros
        if day_range:
            target_date = datetime.now() - timedelta(days=day_range)
            values = values.filter(date__gte=target_date)

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
        }
        return render(request, 'extract/view_extract.html', context)
    
'''
def export_extract(request):
    values = Values.objects.filter(date__month=datetime.now().month)
    accounts = Account.objects.all()
    categories = Category.objects.all()
    
    path_template = os.path.join(settings.BASE_DIR, 'extract/templates/extract/export_extract.html') 
    path_output = BytesIO()

    template_render = render_to_string(path_template, {'values': values, 'accounts': accounts, 'categories': categories})
    HTML(string=template_render).write_pdf(path_output)

    path_output.seek(0)
    

    return FileResponse(path_output, filename="extrato.pdf")
'''
