from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    club = models.ManyToManyField(Club)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

