from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    first_name=serializers.CharField(required=False)
    last_name=serializers.CharField(required=False)
    company_name=serializers.CharField(required=False)
    city=serializers.CharField(required=False)
    state=serializers.CharField(required=False)
    zip=serializers.IntegerField(required=False)
    email=serializers.CharField(required=False)
    web=serializers.CharField(required=False)
    age=serializers.IntegerField(required=False)

    class Meta:
        model=User
        fields='__all__'
