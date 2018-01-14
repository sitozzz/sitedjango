from django.db import models


class Profiles(models.Model):
    Name = models.CharField(max_length=30)

    Email = models.EmailField()
    Phone = models.IntegerField(max_length=11)

    def __str__(self):
        return self.Name
