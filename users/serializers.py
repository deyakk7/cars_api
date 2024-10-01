from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    confirmed_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirmed_password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if attrs["password"] != attrs["confirmed_password"]:
            raise ValidationError("Entered passwords mismatched")

        attrs.pop("confirmed_password")

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        email = attrs.get("email")
        password = attrs.get("password")

        if not (username or email):
            raise ValidationError({"error": "Username or email is required"})

        if username and email:
            raise ValidationError(
                {"error": "Either username or email should be provided"}
            )

        user = User.objects.filter(Q(username=username) | Q(email=email)).first()

        if user is None:
            raise ValidationError({"error": "Invalid credentials"})

        if not user.check_password(password):
            raise ValidationError({"error": "Invalid credentials"})
        attrs["user"] = user

        return attrs

    def create(self, validated_data):
        return validated_data.get("user")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.is_superuser = validated_data.get(
            "is_superuser", instance.is_superuser
        )

        password = validated_data.get("password")

        if password:
            instance.set_password(password)

        instance.save()
        return instance
