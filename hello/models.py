from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cart = models.JSONField(max_length=50)
    profileImage = models.BinaryField()
    profileImageName = models.CharField(max_length=50)
    isActive = models.BooleanField()
    emailVerified = models.BooleanField()

    def __str__(self):
        return self.username
