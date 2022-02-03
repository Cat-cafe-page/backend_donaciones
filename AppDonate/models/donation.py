from django.db import models

class Donation(models.Model):
    id_donation = models.BigAutoField(primary_key=True)
    email       = models.EmailField('Email', max_length=100)
    cardNumber  = models.IntegerField('Numero de tarjeta')
    nameOnCard  = models.CharField('Nombre en la tarjeta', max_length=50)
    amount      = models.IntegerField(default=0)
    city        = models.CharField('Ciudad', max_length=30)
