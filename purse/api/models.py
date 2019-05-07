from django.db import models
from django.conf import settings
from django.contrib import admin


class CoinName(models.Model):
    name = models.CharField(max_length=20)
    symbol = models.CharField(max_length=5)

    def __str__(self):
        result = '{}({})'.format(self.name, self.symbol)
        return result


class Purse(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        result = '{} ({})'.format(self.name, self.owner.username)
        return result


class Coin(models.Model):
    purse = models.ForeignKey(Purse, related_name='coins', on_delete=models.CASCADE)
    coin_name = models.ForeignKey(CoinName, on_delete=models.CASCADE)
    volume = models.FloatField()

    def __str__(self):
        return '{}: {}'.format(self.coin_name.name, self.volume)


admin.site.register(CoinName)
admin.site.register(Purse)
admin.site.register(Coin)
