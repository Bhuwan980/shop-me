from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User

# Create your models here.
class MyAccountManager(BaseUserManager):
    #creating the normal user
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        if not username: 
            raise ValueError('Enter Username')
        user = self.model(
            #it will lowercased the all the uppercase character of domain of email
            email = self.normalize_email(email),
            first_name = first_name, 
            last_name = last_name, 
            username = username,
    
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    

    #creating the superuser
    def create_superuser(self, first_name, last_name, username, email, password):
        if not email: 
            raise ValueError('Please enter the email')
        if not username:
            raise ValueError('enter the username')
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password = password, 
            first_name = first_name,
            last_name = last_name ,
          
           


        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser =  True
        user.save(using  = self._db)
        return user



class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=10)

    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    objects = MyAccountManager()

    #for login using the email
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    # this will return true if required permission is assigned else return false
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    #it always return true for active user/superuser and false for not active user 
    def has_module_perms(self, add_label):
        return True
