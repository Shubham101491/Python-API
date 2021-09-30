from django.db import models

class Vard1(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.IntegerField()
    profession = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
