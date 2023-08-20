
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

class ContactFormView(APIView):
    def post(self, request):
        data = request.data

        # Verificar que el objeto JSON tenga los campos necesarios
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if field not in data:
                return Response({'error': f'Missing field: {field}'}, status=status.HTTP_400_BAD_REQUEST)

        # Extraer los datos del objeto JSON
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        # Enviar el correo electrónico
        try:
            send_mail(
                subject,
                f'Nombre: {name}\nEmail: {email}\nMensaje: {message}',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],  # Reemplaza con la dirección de correo destino
                fail_silently=False,
            )
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
