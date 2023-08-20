import services.serializer as serializer
import services.models as service

from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token

class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            return None
        return (token.user, token)


class RitosDePasoViewSet(viewsets.ModelViewSet):
    queryset = service.RitosDePaso.objects.all()
    serializer_class=serializer.ritospasoSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)



class AlquimiaViewSet(viewsets.ModelViewSet):
    queryset = service.Alquimia.objects.all()
    serializer_class=serializer.alquimiaSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)
    



class CartografiaViewSet(viewsets.ModelViewSet):
    queryset = service.Cartografia.objects.all()
    serializer_class=serializer.cartografiaSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)



class DueloGestacionalViewSet(viewsets.ModelViewSet):
    queryset = service.DueloGestacional.objects.all()
    serializer_class=serializer.dueloSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)
    



class FloresViewSet(viewsets.ModelViewSet):
    queryset = service.Flores.objects.all()
    serializer_class=serializer.floresSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)
    



class GestarParirAlumbrarViewSet(viewsets.ModelViewSet):
    queryset = service.GestarParirAlumbrar.objects.all()
    serializer_class=serializer.gestarSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)
    



class HierbasBañosYVaporesViewSet(viewsets.ModelViewSet):
    queryset = service.HierbasBañosYVapores.objects.all()
    serializer_class=serializer.hierbasSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)
    



class MasajeViewSet(viewsets.ModelViewSet):
    queryset = service.Masaje.objects.all()
    serializer_class=serializer.masajeSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)
    



class RitualCerradaViewSet(viewsets.ModelViewSet):
    queryset = service.RitualCerrada.objects.all()
    serializer_class=serializer.cerradaSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)
    



class TejedoraViewSet(viewsets.ModelViewSet):
    queryset = service.Tejedora.objects.all()
    serializer_class=serializer.tejedoraSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)
    
