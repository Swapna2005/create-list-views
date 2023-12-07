from django.db import models

class RegisterModel(models.Model):
    Username=models.CharField(max_length=256)
    Email=models.CharField(max_length=256)
    Password=models.TextField()
    def __str__(self) -> str:
        return self.Username


