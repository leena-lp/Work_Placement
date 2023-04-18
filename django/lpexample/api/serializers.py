from rest_framework import serializers



from django.contrib.auth.models import User


from .models import Employee


class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","password"]

    

class RegisterSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True,write_only=True)
    class Meta:
        model=User
        fields=["id","first_name","last_name","username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employee
        fields=["id","name","dept","salary","gender","address","profilepic"]

    




