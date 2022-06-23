from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loan/', views.loan, name='loan'),
    path('crypt/', views.crypt, name='crypt'),
    path('products/', views.products, name='products'),
    path('spiral/', views.spiral, name='spiral')
]