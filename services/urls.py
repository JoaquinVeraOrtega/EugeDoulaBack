from django.urls import path,include
from rest_framework import routers
from services import views

router=routers.DefaultRouter()
router.register(r'tejedora',views.TejedoraViewSet)
router.register(r'cartografia',views.CartografiaViewSet)
router.register(r'masaje',views.MasajeViewSet)
router.register(r'cerrada',views.RitualCerradaViewSet)
router.register(r'hierbas',views.HierbasBañosYVaporesViewSet)
router.register(r'ritos de paso',views.RitosDePasoViewSet)
router.register(r'gestar',views.GestarParirAlumbrarViewSet)
router.register(r'alquimia',views.AlquimiaViewSet)
router.register(r'flores',views.FloresViewSet)
router.register(r'duelo',views.DueloGestacionalViewSet)

urlpatterns = [
    path('', include(router.urls))
]