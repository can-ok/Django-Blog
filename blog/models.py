from django.db import models
from datetime import datetime    

# Create your models here.


class blog(models.Model):
    title =models.CharField(max_length=20)
    pub_data=models.DateTimeField(default=datetime.now)
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]#give me first 100 hun. char.

    def pub_date_pretty(self):
        return self.pub_data.strftime('%b %e %y')