from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response, data, status

# Create your views here.

@api_view(['POST'])
@permissions_classes(['AllowAny'])
def login(request):
    usuario = request.data.gte('username')
    password = request.data.get('password')

    if not usuario or not password:
        return Response(
            data:{'error': 'Se requiereusuario y contraseña'}
            status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticated(username=usuario, password=password)
@api_view(['POST'])
@permission_classes(['IsAuthenticated'])
def logout(request):
    pass
