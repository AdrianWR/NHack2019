from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import re

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_(‘The given username must be set’))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user   

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(_('username'), 
        max_length=15, 
        unique=True, 
        help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'), 
        validators=[ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))]) 
        max_length=1date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    name = models.CharField(_('name'), max_length=255)

    email = models.EmailField(_('email address'), max_length=255, unique=True)

    endereco = models.CharField(_('endereco'), max_length=255)
    
    cep = models.CharField(_('cep'), max_length=8)

    # Campo exclusivo para doadores
    cpf = models.CharField(_('cpf'), max_length=11)

    # Campo exclusivo para ONGs
    cnpj = models.CharField(_('cnpj'), max_length=13, unique=True)

    # Verifica se usuário verificou e-mail
    is_trusty = models.BooleanField(_('trusty'), default=False, help_text=_('Designates whether this user has confirmed his account.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])