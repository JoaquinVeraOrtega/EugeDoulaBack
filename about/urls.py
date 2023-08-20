from django.urls import path,include
from rest_framework import routers
from about import views

router=routers.DefaultRouter()
router.register(r'',views.AboutViewSet)

urlpatterns = [
    path('', include(router.urls))
]