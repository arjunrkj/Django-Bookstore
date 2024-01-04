from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    desc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image')
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name