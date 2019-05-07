from rest_framework import serializers
from . import models
from django.utils.translation import gettext_lazy as _


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(read_only=True)

    def validate(self, data):
        try:
            user = models.User.objects.filter(username=data.get('username'))
            if len(user) > 0:
                raise serializers.ValidationError(_("Username already exists"))
        except models.User.DoesNotExist:
            pass

        # if not data.get('password') or not data.get('confirm_password'):
        #     raise serializers.ValidationError(_("Empty Password"))
        #
        # if data.get('password') != data.get('confirm_password'):
        #     raise serializers.ValidationError(_("Mismatch"))

        return data

    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name', 'password', 'confirm_password', 'is_active')
