from django.db import models

# Create your models here.
class Name(models.Model):
    name=models.CharField(max_length=250)
    date=models.DateField()
    image=models.ImageField(upload_to='todoimage')
    
    
    def __str__(self):
        return self.name