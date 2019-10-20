from django.db import models


# Create your models here.

#class UserManager(BaseUserManager):
#    
#    def create_user(self, username, email, password, **extra_fields):
#        now = timezone.now()
##        if not username:
##            raise ValueError('The given username must be set')
 #       email = self.normalize_email(email)
 #       user = self.model(username=username, email=email, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
  #      user.set_password(password)
   #     user.save(using=self._db)
    #    return user

class ConnectUser(models.Model):
    
    username = models.CharField('username', 
        max_length=15, 
        unique=True)
        
    name = models.CharField('name', max_length=255)

    email = models.EmailField('email address', max_length=255, unique=True)

    endereco = models.CharField('endereco', max_length=255)
    
    cep = models.CharField('cep', max_length=8)

    # Campo exclusivo para doadores
    cpf = models.CharField('cpf', max_length=11)

    # Campo exclusivo para ONGs
    cnpj = models.CharField('cnpj', max_length=13, unique=True)

    # Verifica se usuário verificou e-mail
    is_trusty = models.BooleanField('trusty', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    #objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    