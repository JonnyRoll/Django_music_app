from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length= 50, null= False, unique= True)
    creation_date = models.DateField(auto_now_add= False, null= False)
    description = models.CharField(max_length= 200, null = True)

