import re

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from braces.views import CsrfExemptMixin
from oauth2_provider.views.mixins import OAuthLibMixin


class UserRegister(CsrfExemptMixin, OAuthLibMixin, APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data

        password = data.get('password')
        c_password = data.get('confirm_password')
        username = data.get('username')

        if request.user.is_authenticated:
            msg = 'You also have account'
            return Response(data={"error": msg}, status=status.HTTP_403_FORBIDDEN)

        if not re.findall("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})", password):
            msg = 'Bad password'
            return Response(data={"error": msg}, status=status.HTTP_400_BAD_REQUEST)

        if not password or not c_password:
            msg = 'Missed or empty `password` or `confirm_password`'
            return Response(data={"error": msg}, status=status.HTTP_400_BAD_REQUEST)

        if password != c_password:
            msg = 'Differ `password` and `confirm_password`'
            return Response(data={"error": msg}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username):
            msg = 'Username `{}` is required'.format(username)
            return Response(data={"error": msg}, status=status.HTTP_400_BAD_REQUEST)

        user = User(username=username)
        user.set_password(password)
        user.save()

        return Response(data={"success": True}, status=status.HTTP_201_CREATED)