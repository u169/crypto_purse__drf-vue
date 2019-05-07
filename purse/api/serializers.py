from rest_framework import serializers
from . import models


class CoinNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoinName
        fields = ('name', 'symbol')


class CoinSerializer(serializers.ModelSerializer):
    coin_name = CoinNameSerializer()

    class Meta:
        model = models.Coin
        fields = ('pk', 'coin_name', 'volume')


class PurseSerializer(serializers.ModelSerializer):
    coins = CoinSerializer(many=True)

    class Meta:
        model = models.Purse
        fields = ('name', 'coins')
