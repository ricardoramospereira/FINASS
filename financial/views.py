from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Account, Category
from extract.models import Values
from django.contrib.messages import constants
from django.contrib import messages
from django.core.paginator import Paginator, Page


# Create your views here.
def financial_index(request):
    accounts = Account.objects.all()

    paginator = Paginator(accounts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    total_balance = sum(account.value for account in accounts)  # Total de todos os valores

    context = {
         'accounts': accounts,
         'total_balance': total_balance,
         'page_obj': page_obj
    }

    return render(request, 'financial/financial_index.html', context)


def manage_financial(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        category = Category.objects.all()

        paginator = Paginator(accounts, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


        context = {
            "accounts": accounts,
            "category": category,
            "page_obj": page_obj
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
             if (len(bank.strip()) ==0 ) or (len(type.strip()) ==0 ) or (len(value.strip()) ==0 ):
                 messages.add_message(request, constants.ERROR, "Todos os campos devem ser preenchidos")
                 return redirect('/finantial/manage_financial/')

        account = Account(
             bank = bank,
             type = type,
             value = value
        )

        account.save()
        messages.add_message(request, constants.SUCCESS, "Banco cadastrado com sucesso")

        return redirect('/finantial/manage_financial/')


def delete_bank(request, id):
     bank = Account.objects.get(id=id)
     bank.delete()
     messages.add_message(request, constants.SUCCESS, "Banco excluido com sucesso")
     return redirect('/finantial/manage_financial/')


def register_category(request):
    if request.method == "GET":
        return render(request, 'financial/manage_financial.html')  # Certifique-se de passar o nome do template correto

    elif request.method == "POST":
        category_name = request.POST.get('category')
        essential_value = request.POST.get('essential')
        essential = essential_value == 'on'  # Converte para valor booleano

        # TODO: Validações

        category = Category(
            category=category_name,
            essential=essential
        )

        category.save()

        messages.success(request, 'Categoria cadastrada com sucesso')  # Use messages.success para mensagens de sucesso

        return redirect('/finantial/manage_financial/')
    
##################### parei aqui ######################
def delete_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        associated_values = Values.objects.filter(category=category)

        if associated_values.exists():
            messages.add_message(request, constants.ERROR, "Não é possível excluir a categoria, pois existem valores associados a ela.")
            return redirect('/finantial/manage_financial/')  # Redireciona de volta à página de listagem de categorias

        category.delete()
        messages.add_message(request, constants.SUCCESS, "Categoria excluída com sucesso.")
        return redirect('/finantial/manage_financial/')

    except Category.DoesNotExist:
        messages.add_message(request, constants.WARNING, "Categoria não encontrada.")
        return redirect('/finantial/manage_financial/')

    
def update_category(request, id):
     category = Category.objects.get(id=id)

     category.essential = not category.essential

     category.save()

     return redirect('/finantial/manage_financial/')


