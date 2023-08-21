from django.db import models

# Create your models here.

class contactform(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    mode_of_contact = models.CharField('Conatct by', max_length=50)
   
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email