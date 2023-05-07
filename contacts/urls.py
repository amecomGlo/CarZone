from django.urls import path

from . import views

urlpatterns = [
    path('inquiry/<slug:slug>/', views.inquiry, name='inquiry')
]