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

    




from django.contrib.auth import authenticate, user_logged_in

from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler

class JWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(request=self.context['request'], **credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)
                user_logged_in.send(sender=user.__class__, request=self.context['request'], user=user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "{username_field}" and "password".'
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)
