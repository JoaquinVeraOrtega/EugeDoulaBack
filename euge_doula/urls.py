from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('docs/', include_docs_urls(title='Api Documentation')),
    path('home/', include('home.urls')),
    path('services/', include('services.urls')),
    path('cielo/', include('cielo.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('testimonial/', include('testimonial.urls')),
]
