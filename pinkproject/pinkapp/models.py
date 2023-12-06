from django.db import models

class ForgettModel(models.Model):
    Email=models.EmailField(max_length=256)
    phone=models.TextField()
    Password=models.TextField()
    def __str__(self) -> str:
        return self.Email

