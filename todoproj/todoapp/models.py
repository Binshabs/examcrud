from django.db import models

# Create your models here.
class Name(models.Model):
    name=models.CharField(max_length=250)
    mark=models.IntegerField()
    date=models.DateField()
    image=models.ImageField(upload_to='imageS')
    
    
    def __str__(self):
        return self.name