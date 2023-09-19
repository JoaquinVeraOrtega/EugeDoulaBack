from .serializer import PostSerializer
from .models import Blog

from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.pagination import LimitOffsetPagination

class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            return None
        return (token.user, token)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class=PostSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def check_permissions(self, request):
        if self.action in ['list', 'retrieve']:
            return
        return super().check_permissions(request)
