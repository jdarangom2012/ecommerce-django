from operator import truediv
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountsManager(BaseUserManager):
    def CreateUser(self, firts_name, last_name, user_name, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email')
        if not user_name:
            raise ValueError('El usuario debe tener un username')
        
        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            firts_name = firts_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firts_name, last_name, email, user_name, password):
        user = self.CreateUser(
            email = self.normalize_email(email),
            user_name = user_name,
            password = password,
            firts_name = firts_name,
            last_name = last_name,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True #permite la autenticacion
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser):
    firts_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)


    #Campos Atributos de django

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'firts_name', 'last_name']

    objects = MyAccountsManager()

    def __str__(self): 
        return self.email
    
    def has_perm(self, perm, obj=None): #Si tiene permisos
        return self.is_admin
    
    def has_module_perms(self, add_label):#Si tiene acceso a los modulos
        return True
        




        

