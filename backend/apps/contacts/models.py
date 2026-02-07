from django.db import models
#from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        if not email:
            raise ValueError("Email address is required.")
        email = self.normalize_email(email)
        user = self.model(email = email, first_name = first_name)
        user.set_password(password)
        user.save()
        return user
    
    def create_super_user(self, email, first_name, password = None):
        if not email:
            raise ValueError("Email address is required.")
        email = self.normalize_email(email)
        user = self.model(email = email, first_name = first_name, is_staff = True)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser,PermissionsMixin,BaseUserManager):
    email = models.EmailField(blank = False,null=False, unique=True, max_length=300)
    first_name = models.CharField(blank=False,null=True)
    last_name = models.CharField(blank=False,null=True)
    notes = models.TextField(blank=True)
    is_staff = models.BooleanField(blank=True,default=False,null = True)
    is_active = models.BooleanField(blank=True,default=True,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now= True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [email, first_name]

    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        ordering = ["first_name"]
        db_table = "users"
        db_table_comment = "A custom user built for the stake holders"



"""
# EXTENDING THE BUILT IN USER ONLY

User = settings.AUTH_USER_MODEL # for scalability and any future changes like custom user

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User,related_name="contact",on_delete=models.SET_NULL, null=True)
    address = models.TextField(blank=True,null =True)

    def __str__(self):
        return f"{self.user.username} : {self.user.first_name} {self.user.last_name}"
"""

