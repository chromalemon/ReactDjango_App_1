from django.shortcuts import render
from .models import FoodItem
from .serializers import serialize_foods
from django.http import JsonResponse

# Create your views here.

def food_list(request):
    foods = FoodItem.objects.all()
    return JsonResponse(serialize_foods(foods), safe=False)

