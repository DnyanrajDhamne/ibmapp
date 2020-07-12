from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField( primary_key = True )
    first_name = models.CharField( max_length=100 )
    last_name = models.CharField( max_length=100 )
    email = models.EmailField( max_length=50, null=False, unique=True )
    phone_number = models.CharField( max_length=10, unique=True )
    password = models.CharField( max_length=250 )



