from django.db import models


class Drop(models.Model):
    dropName = models.TextField(max_length=200)
    dropValue = models.IntegerField()
    dropCount = models.IntegerField(default=0)

    def __str__(self):
        return self.dropName


class GrindZone(models.Model):
    zoneName = models.TextField(max_length=200)
    persons = models.IntegerField()
    drops = models.ManyToManyField(Drop)

    def __str__(self):
        return self.zoneName

"""
TODO
* uzaleznic warosc od funkcji zewnetrznej
* uzaleznic nazwe dopa od kodu w grze
* dodac ikonke dropa
* doddac pola jak nizej:
class OrcCamp(models.Model):
    hours = models.IntegerField()
    minutes = models.IntegerField()
    agris = models.IntegerField()
    trash = models.IntegerField()
    boss = models.IntegerField()
* dodac uzytkownikow
* dodac sesje dla uzytkownika
"""





