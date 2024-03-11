from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager,User,AbstractUser
from django.utils import timezone


# Create your models here.

# class CustomUserManager(UserManager):
#     def create_user(self, username, password, **extra_fields: Any) -> Any:

#         # if not email:
#         #     raise ValueError("email must be specified")

#         if not username:
#             raise ValueError('the username is required ')
        
#         #normalisation de email 
#         # email = self.normalize_email(email)
#         user = self.model(username=username,
#                         #    email=email,
#                             **extra_fields)
#         #hachage du mot de passe 
#         user.set_password(password)
#         user.save(using=self._db)
#     def create_superuser(self,username,password,**extre_fields):
#         extre_fields.setdefault('is_staff' ,True)
#         extre_fields.setdefault('is_superuser',True)

#         return self.create_user(username,password,**extre_fields)

# class CustomUser(AbstractBaseUser):
#     username = models.CharField(max_length = 127,unique = True)
#     email = models.CharField(max_length =255)
#     password = models.CharField(max_length =255)
#     phone_number = models.CharField(max_length=127)
#     is_active =models.BooleanField(default = True)
#     is_staff = models.BooleanField(default = False)
#     is_superuser = models.BooleanField(default = False)
  
#     last_login = models.DateTimeField(
#         ("last login"),
#         default=timezone.now,
#         help_text=("Date and time when this user last logged in."),
#     )
#     date_joined = models.DateTimeField(
#         ("date joined"),
#         default=timezone.now,
#         help_text=("Date and time when this user joined."),
#     )

#     objects =CustomUserManager()

#     USERNAME_FIELD = "username"
#     # EMAIL_FIELD = "email"
#     REQUIRED_FIELDS = []

#     # class Meta:
#     #     abstract = True

#     def get_full_name(self):
#         return self.username

#     def get_short_name(self):
#         return self.username
    
#     def has_perm(self,perm,obj=None):
#         "L'utilisateur a-t-il une autorisation spécifique ?"

#         return True
    
#     def has_module_perms(self,app_label):
#         "L'utilisateur dispose-t-il des autorisations nécessaires pour voir l'application ?`app_label`?"

#         return True
#     def has_perms(self, perm_list, obj=None):
#         """
#             Return True if the user has each of the specified permissions. If
#             object is passed, check if the user has all required perms for it.
#         """
   
#         return True


#     def has_parm():
#         return True

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN  = "admin",
        CLIENT = "client",
        MARCHAND='marchand'
    base_role = Role.ADMIN

    role = models.CharField(max_length=32,choices=Role.choices)

    def save(self,*args,**kwargs):
        self.role = self.base_role
        return super().save(*args,**kwargs)

#table des clients
class Client(CustomUser):
    # user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='client')
    base_role = CustomUser.Role.CLIENT

#table des marchands
class Marchand(CustomUser):
    # user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name = 'marchand')
    base_role = CustomUser.Role.MARCHAND





#table des administarteurs 
class Admin(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)




