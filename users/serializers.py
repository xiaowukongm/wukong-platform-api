from .models import Users
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        module = Users
        fields = ('username','eamil','mobile_phone','password')