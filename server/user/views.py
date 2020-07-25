from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt

from .serializers import UserSerializer


from .models import User


class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetAuthUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = (JSONWebTokenAuthentication,)

    def create(self, request):
        data = request.data
        print(data)
        return Response({'message': data})

    # def get_queryset(self):
    #     queryset =


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication, ])
# @permission_classes([IsAuthenticated])
def GetUser(request):
    data = request.data
    token = data['token']
    decoded = jwt.decode(token, verify=False)
    user_id = decoded['user_id']
    queryset = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(queryset, many=False)
    return Response(serializer.data)

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
