from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def financial_index(request):
    return render(request, 'financial/financial_index.html')

def manage_financial(request):
    return render(request, 'financial/manage_financial.html')
