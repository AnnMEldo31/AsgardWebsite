from django.db import models

class Item (models.Model):
    name = models.CharField(max_length=200, default='Item')
    text = models.CharField(max_length=300, default='Lorem ipsum')

    def __str__(self) -> str:
        return self.name + ": " + self.text