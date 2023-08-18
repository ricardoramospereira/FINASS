from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from investments.models import Investment
from financial.models import Account


# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    if request.method == "GET": # test
        investments = Investment.objects.all()
        balances = Account.objects.all()

        total_balances = sum(balance.value for balance in balances)
        total_investment = sum(investment.value for investment in investments)  # Total de todos os valores

        context = {
            "investments": investments,
            "total_investment": total_investment,
            "total_balances": total_balances,
        }

        return render(request, 'dashboard/index.html', context)
