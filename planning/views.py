from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from financial.models import Category
# tirar o csrf token, devido ao javascript
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def define_planning(request):
    categories = Category.objects.all()

    context = {
        'categories':categories,
    }

    return render(request, 'planning/define_planning.html', context)

@csrf_exempt # isenta essa função do csrf token
def update_value_category(request, id):
    new_value = json.load(request)['new_value']
    category = Category.objects.get(id=id)
    category.planning_value = new_value
    category.save()

    return JsonResponse({'status': 'Sucesso'})