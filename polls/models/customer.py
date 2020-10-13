from django.db import models

class Customer(models.Model):
    fname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def register(self):
        self.save()