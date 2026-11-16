from rest_framework import serializers
from proApp.models import inventoryModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

class inventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=inventoryModel
        fields="__all__"
        read_only_fields=['owner','id','created_at']


    def validate_price(self, k):
        if k<0:
            raise serializers.ValidationError(
                "negative price!!"
            )
        return k