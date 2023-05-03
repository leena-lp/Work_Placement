from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout 

# Create your views here.

from .serializers import RegisterSerializer,EmployeeSerializer
from.models import Employee

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response


from datetime import datetime

from rest_framework.response import Response


from drf_spectacular.utils import extend_schema


from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .email import sent_details_via_email


from activity_log.mixins import ActivityLogMixin



class UserView(ActivityLogMixin,APIView):
    # serializer_class=RegisterSerializer
    # model=User
    # queryset=User.objects.all()
    @extend_schema(
        request=RegisterSerializer,
        responses={201: RegisterSerializer},
    )
    def get(self,request,*args,**kwargs):
        qs=User.objects.all()
        serializer=RegisterSerializer(qs,many=True)
        return Response(data=serializer.data)
    

    @extend_schema(
        request=RegisterSerializer,
        responses={201: RegisterSerializer},
    )
    def post(self,request,*args,**kwargs):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            data=serializer.validated_data


            email=data.get("email")
            username=data.get("username")
            password=data.get("password")
            serializer.save()

            


            print('======================================================================')
            print(email)
            print(username)
            print(password)
            print("==========================================")


            sent_details_via_email(email=email,username=username,password=password)
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
    





class EmployeeView(ActivityLogMixin,viewsets.ModelViewSet):
    
    serializer_class=EmployeeSerializer
    
    model=Employee
    queryset=Employee.objects.all()
    permission_classes=[IsAuthenticated]
    http_method_names=["get"]
    

    @extend_schema(responses=EmployeeSerializer
    )
    def list(self, request, *args, **kwargs):
        qs=Employee.objects.filter(user=request.user)
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    





class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'POST' or request.method == 'GET' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False



class EmployeeDetailView(ActivityLogMixin,viewsets.ModelViewSet):
    serializer_class=EmployeeSerializer
    
    model=Employee
    queryset=Employee.objects.all()
    permission_classes=[IsAdminUser]




class LogoutView(ActivityLogMixin,APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            logout_time=datetime.now()
            print(logout_time)
            print(token)
            
            token.blacklist()

            return Response("Successful Logout", status=status.HTTP_200_OK)