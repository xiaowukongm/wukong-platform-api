from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializers
from .models import Users


# Create your views here.
def login(request):
    return HttpResponse("")

def register(request):
    pass

class User(APIView):
    def get(self,request,format=None):
        user = Users.objects.get(id=1)
        username = user.username
        eamil = user.eamil
        mobile_phone = user.mobile_phone
        password = user.password
        resp = {
           'username' :username,
           'eamil' :eamil,
           'mobile_phone' :mobile_phone,
           'password' :password,
        }
        return Response(resp)