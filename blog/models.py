from django.db import models
from datetime import datetime    

# Create your models here.


class blog(models.Model):
    title =models.CharField(max_length=20)
    pub_data=models.DateTimeField(default=datetime.now)
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
    