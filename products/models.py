from django.db import models

# Create your models here.
class Policy(models.Model):
    name = models.CharField(max_length=100)
    premium = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()


