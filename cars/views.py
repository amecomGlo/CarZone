from itertools import chain
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, Page
from .models import *
from django.db.models import Q
from django.views.generic import ListView
# Create your views here.

class CarListView(ListView):
    paginate_by = 4
    model = Car
    template_name = 'cars/cars.html'
    
        
    def get_context_data(self, **kwargs):
        data = super(CarListView, self).get_context_data(**kwargs)
        model_search = set(Car.objects.values_list('model', flat=True))
        data['model_search'] = model_search
        city_search = set(Car.objects.all().values_list('city', flat=True))
        data['city_search'] = city_search
        body_style_search = set(Car.objects.values_list('body_style', flat=True))
        data['body_style_search'] = body_style_search
        year_search = set(Car.objects.values_list('year', flat=True))
        data['year_search'] = year_search
    
        return data
      


def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    
    context = {
        'item': car,
    }
    return render(request, 'cars/detail.html', context)


def search(request):
    cars = Car.objects.order_by('-created_at')
    model_search = set(Car.objects.values_list("model", flat=True))
    year_search = set(Car.objects.values_list('year', flat=True))
    city_search = set(Car.objects.values_list('city', flat=True))
    body_style_search = set(Car.objects.values_list('body_style', flat=True))
    if 'q' in request.GET:
        q = request.GET.get('q', '')
        if q:
            cars = Car.objects.filter(Q(title__icontains=q)|Q(description__icontains=q)|Q(model__icontains=q))
    
    if 'model' in request.GET:
        model = request.GET.get('model', '') 
        if model:
            cars = Car.objects.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET.get('city', '') 
        if city:
            cars = Car.objects.filter(city__iexact=city)
            
    if 'year' in request.GET:
        year = request.GET.get('year', '') 
        if year:
            cars = Car.objects.filter(year__iexact=year)
    

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = Car.objects.filter(body_style__iexact=body_style)
    
    if 'min_price' in request.GET:
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if max_price:
            Car.objects.filter(price__gte=min_price, price__lte=max_price)
    
    context = {
        'cars': cars,
        'model_search': model_search,
        'year_search': year_search,
        'city_search': city_search,
        'body_style_search': body_style_search,
    }
    
    return render(request, 'cars/search.html', context)
        