from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # всего цифр 10 из них 2 после запятой
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]  # добавил ограничение по возрасту
    )

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()  # описание с неограниченным количеством текста
    age_limited = models.BooleanField(default=False)  # ограничение по возрасту 18+ (булево поле по дефолту False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title