from django.urls import path
from . import views
from .views import (
    CarListView,
)


app_name = 'product'
urlpatterns = [
    path('cars', CarListView.as_view(), name='cars'),
    path('search', views.search, name='search'),
    path('<slug:slug>', views.car_detail, name='detail'),
    
]