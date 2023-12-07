from django.db import models

class LoginModel(models.Model):
    Username=models.CharField(max_length=256)
    Password=models.TextField()
    def __str__(self) -> str:
        return self.Username