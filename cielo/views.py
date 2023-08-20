from .serializer import CieloSerializer
from .models import Cielo

from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication , SessionAuthentication
from rest_framework.authtoken.models import Token

class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            return None
        return (token.user, token)


class CieloViewSet(viewsets.ModelViewSet):
    queryset = Cielo.objects.all()
    serializer_class=CieloSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    
    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)