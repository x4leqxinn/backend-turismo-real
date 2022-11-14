from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from apps.base.models.db_models import Persona

class UserRole(models.Model):    
    description = models.CharField('Descripción',max_length=50, blank=False, null=False,unique=True)

    class Meta:
        verbose_name = "Rol de Usuario"
        verbose_name_plural = "Roles de Usuario"
        db_table = 'AUTH_USER_ROLE'

    def __str__(self):
        return self.description


# Create Custom User Manager
class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("No se ha entregado un correo electrónico")

        if not password:
            raise ValueError("No se ha entregado una contraseña")

        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active' ,True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    image = models.ImageField('Imagen de perfil', upload_to='user_profile/', default='', max_length=255, null=True, blank = True)
    role = models.ForeignKey(UserRole, on_delete = models.CASCADE, verbose_name = 'Rol Usuario', null = True)
    person = models.OneToOneField('people.Persona', on_delete = models.CASCADE, verbose_name = 'Persona', null = True)

    is_staff = models.BooleanField(default=False) # must needed, otherwise
    is_active = models.BooleanField(default=True) # must needed, otherwise
    is_superuser = models.BooleanField(default=False) # this field we inherit

    
    objects = CustomUserManager() 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'AUTH_USER_ACCOUNT'