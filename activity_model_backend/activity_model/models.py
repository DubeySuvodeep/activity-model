from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(unique=True, max_length=255)
    location = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.name

class ActivityPeriod(models.Model):
    
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activity')
    start_time = models.DateTimeField()
    end_time =  models.DateTimeField()   
    