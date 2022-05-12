from django.contrib.auth.models import User
from django.db import models

class App_user(models.Model):
    role = models.CharField(max_length=30, choices=(("Patient", "Patient"), ("Doctor", "Doctor")))
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
