from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="Homepage"),
    path('services/', views.services, name="Services"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
    path('subservice/<myservice>/', views.subservice, name="SubServices"),
    path('checkout/<int:myid>/', views.checkout, name="checkoutServices"),
    path('booking/<int:sid>/', views.booking, name="BookService"),
]