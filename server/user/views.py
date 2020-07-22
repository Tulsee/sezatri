from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication


from .serializers import UserSerializer


from .models import User


class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @api_view(['POST'])
# def RegisterUser(request):
#     serializer = UserSerializer(data=request.data)
#     data = {}
#     if serializer.is_valid():
#         user = serializer.save()
#         data['response'] = 'Successfully register a new user'
#     else:
#         data = serializer.errors
#     return Response(data)
