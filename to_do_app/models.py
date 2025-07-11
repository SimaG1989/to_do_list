from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
task_status=[('New','New'),('In Progress','In Progress'),('Completed','Completed')]
class User (AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField(default='')
    username = models.CharField(max_length=255, unique=True)
    password=models.CharField(validators=[MinLengthValidator(6,'Minimum 6 digits' )])

    def __str__(self):
        return self.username
    
class Task (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    status = models.CharField(choices=task_status)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
