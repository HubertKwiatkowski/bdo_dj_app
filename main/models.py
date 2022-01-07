from django.db import models


class Item(models.Model):
    chooseKey = models.IntegerField(null=True)
    count = models.IntegerField(null=True)
    grade = models.IntegerField(default=0)
    keyType = models.IntegerField()
    mainCategory = models.IntegerField()
    mainKey = models.IntegerField()
    name = models.TextField(max_length=200)
    pricePeOne = models.IntegerField(null=True)
    subCategory = models.IntegerField()
    subKey = models.IntegerField()
    totalTradeCount = models.IntegerField(null=True)
    mainLabel = models.TextField(max_length=200)
    subLabel = models.TextField(max_length=200)
    description = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.description