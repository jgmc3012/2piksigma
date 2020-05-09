from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import django.contrib.auth.password_validation as validators

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password', 'username', 'first_name',
                    'last_name', 'email', 'phone', 'dni']
        extra_kwargs = {
            'first_name': {'required': True, 'allow_null': False},
            'last_name': {'required': True, 'allow_null': False},
            'email': {
                'required': True, 'allow_null': False,
                'validators': [UniqueValidator(queryset=User.objects.all())]
            },
            'password' : {
                'validators': [validators.validate_password],
                'write_only': True
            },
        }