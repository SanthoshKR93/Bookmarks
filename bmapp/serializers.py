from rest_framework import serializers,exceptions
from .models import Link
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	def validate(self,data):
		username = data.get("username","")
		password = data.get("password","")
		if username and password:
			user =authenticate(username=username, password=password)
			if user:
				if user.is_active:
					data["user"] = user
				else:
					message = "user is inactive"
					raise exceptions.ValidationError(message)
			else:
				message = "Unable to login with provided credentials."
				raise exceptions.ValidationError(message)
		else:
			message = "Must provide both username and password."
			raise exceptions.ValidationError(message)
		return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username = validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user