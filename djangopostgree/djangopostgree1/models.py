from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


"""Создаем несколько таблиц"""

class Seasons(models.Model):
    name = models.CharField(max_length=50)
    temperature = models.IntegerField()

    def __str__(self):
        return self.name


class Countries(models.Model):
    name = models.CharField(max_length=50)
    population = models.IntegerField()

    def __str__(self):
        return self.name