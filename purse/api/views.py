from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import models, serializers


class PurseList(generics.ListAPIView):
    serializer_class = serializers.PurseSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied('Login please!')
        return models.Purse.objects.filter(owner=user)


class CoinViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = self.__query_set(request)
        return self.__response(queryset, True)

    def create(self, request):
        coin = models.Coin(
            coin_name_id=request.data['coin_name_pk'],
            purse_id=request.data['purse_pk'],
            volume=request.data['volume'])
        coin.save()
        return self.__response(coin)

    def retrieve(self, request, pk=None):
        queryset = self.__query_set(request)
        coin = get_object_or_404(queryset, pk=pk)
        return self.__response(coin)

    def update(self, request, pk=None):
        queryset = self.__query_set(request)
        coin = get_object_or_404(queryset, pk=pk)
        coin.volume = request.data['volume']
        coin.save()
        return self.__response(coin)

    def destroy(self, request, pk=None):
        query_set = self.__query_set(request)
        coin = get_object_or_404(query_set, pk=pk)
        coin.delete()
        return JsonResponse({'success': True})

    @staticmethod
    def __query_set(request):
        user = request.user
        queryset = models.Coin.objects.filter(purse__owner=user)
        return queryset

    @staticmethod
    def __response(queryset, many=False):
        serializer = serializers.CoinSerializer(queryset, many=many)
        return Response(serializer.data)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
