from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Company, Price
from django.http import JsonResponse
from django.core import serializers

def index(request):
    companys = Company.objects.all()
    context = {
        'companys': companys,
    }
    return render(request, 'app_2/index.html', context)

def getPrices(request):
    company_id = request.GET.get('company_id', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    prices = Price.objects.filter(company_id=company_id, date__range=[start_date, end_date]).only('company_id', 'date')
    prices = serializers.serialize("json", prices)
    print(prices)

    data_to_html = {
        'data': prices
    }
    return JsonResponse(data_to_html)
