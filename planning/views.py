from django.shortcuts import render
from django.http import HttpResponse
from financial.models import Category

# Create your views here.
def define_planning(request):
    categories = Category.objects.all()

    context = {
        'categories':categories,
    }

    return render(request, 'planning/define_planning.html', context)

def update_value_category(request, id):
    pass