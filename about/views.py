from .serializer import AboutSerializer
from .models import About

from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication 
from rest_framework.authtoken.models import Token

class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            return None
        return (token.user, token)



class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class=AboutSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    
    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)