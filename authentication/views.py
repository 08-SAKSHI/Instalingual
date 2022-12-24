from django.shortcuts import render,HttpResponse
from serializers import RegisterSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from models import RegisterUser
# Create your views here.


# class RegistrationViewSet(viewsets.ModelViewSet):
#     user = RegisterUser.objects.all()
#     serializer_class = RegisterSerializer(user,many = True)
    
def RegistrationViewSet(request):
    user = RegisterUser.objects.all()
    serializer_class = RegisterSerializer(user,many = True)
    json_data = JSONRenderer().render(serializer_class.data)
    return HttpResponse(json_data,content_type='application/json')