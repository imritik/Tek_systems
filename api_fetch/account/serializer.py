from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from account.models import Temp 


class TempSerializer(serializers.ModelSerializer):
    uid =serializers.IntegerField()
    name =serializers.CharField(max_length=100)
    address =serializers.CharField(max_length=100)
    gender=serializers.CharField(max_length=100,default='m')
    pincode=serializers.IntegerField(default=24510)
    
    class Meta:
        model = Temp 
        fields = ['uid', 'name', 'address','pincode','gender']

    def create(self, validated_data):
        return Temp.objects.create(**validated_data)

