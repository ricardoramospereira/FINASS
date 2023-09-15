from django.shortcuts import render, redirect
from financial.models import Category
from .models import Bill_to_pay, PaidBills
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime

# Create your views here.
def accounts(request):
    if request.method == "GET":
        categories = Category.objects.all()

        context = {
            'categories': categories
        }

        return render(request, 'accounts/accounts.html', context)
    
    elif request.method == "POST":
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        value = request.POST.get('value')
        bill_day = request.POST.get('bill_day')


        if any(x is None or len(x.strip()) == 0 for x in [title, category, description, value, bill_day]):
            messages.add_message(request, constants.ERROR, "Todos os campos devem ser preenchidos")
            return redirect('/accounts/')
                
        else:
            account = Bill_to_pay(
                title=title,
                category_id=category,
                description=description,
                value=value,
                bill_day=bill_day
            )
            try:
                account.save()
                messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')
                return redirect('/accounts/')
            
            except:
                messages.add_message(request, constants.WARNING, 'Erro interno do sistema')
                return redirect('/accounts/')


def see_accounts(request):
    current_date = datetime.now().date()

    # Obter IDs de contas pagas no mês atual
    paid_account_ids = PaidBills.objects.filter(date_bill__month=current_date.month).values_list('account_id', flat=True)

    # Obter contas que estão vencidas e não foram pagas
    overdue_account = Bill_to_pay.objects.filter(bill_day__lt=current_date).exclude(id__in=paid_account_ids)

    return render(request, 'accounts/see_accounts.html', {'overdue_account': overdue_account})