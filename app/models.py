from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Book(models.Model):
    STATUS_CHOICES = [
        ('Mavjud', 'Mavjud'),
        ('Band', 'Band'),
    ]

    nomi = models.CharField(max_length=255)
    muallifi = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    holati = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    oluvchi = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    olingan_sanasi = models.DateField(null=True, blank=True)
    beriladigan_sanasi = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nomi} - {self.author} ({self.get_status_display()})"

    def get_absolute_url(self):
        return reverse('detal',args=[str(self.pk)])

   

