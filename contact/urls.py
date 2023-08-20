from django.urls import path
from .views import ContactFormView

urlpatterns = [
    # Otras URLs de tu API
    path('contact/', ContactFormView.as_view(), name='contact-form'),
]
