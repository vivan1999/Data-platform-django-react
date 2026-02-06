from django.db import models
#from django.contrib.auth.models import User

from django.conf import settings

User = settings.AUTH_USER_MODEL # for scalability and any future changes like custom user

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User,related_name="contact",on_delete=models.SET_NULL, null=True)
    address = models.TextField(blank=True,null =True)

    def __str__(self):
        return f"{self.user.username} : {self.user.first_name} {self.user.last_name}"