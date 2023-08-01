from django.forms import ValidationError
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, Serializer
from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model, authenticate


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


UserModel = get_user_model()


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(
            email=clean_data['email'], password=clean_data['password'])
        user_obj.username = clean_data['username']
        user_obj.save()
        return user_obj


class UserLoginSerializer(Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    ##

    def check_user(self, clean_data):
        user = authenticate(
            username=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError('user not found')
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')
