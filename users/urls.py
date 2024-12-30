# urls.py

from django.urls import path
from .views import subscribe, contact_form, handle_booking

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('contact/',contact_form, name='contact_form'),
    path('booking/',handle_booking, name='handle_booking'),  
]
