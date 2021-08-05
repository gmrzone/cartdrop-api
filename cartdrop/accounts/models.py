from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone
from .utils import user_photo_location
# Create your models here.


class CustomUserManager(BaseUserManager):
    pass


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class UserTypes(models.TextChoices):
        customer = 'customer', 'Customer'
        seller = 'seller', 'Seller'

    username_validators = UnicodeUsernameValidator()

    number = models.CharField(_("Mobile Number"), max_length=10, unique=True, db_index=True, error_messages={'unique': _("This number is already registered with us please try logging in")})
    email = models.EmailField(_("Email address"), max_length=50, unique=True, error_messages={'unique': _('A user with this email already exist')})
    username = models.CharField(_('Username'), max_length=50, unique=True, validators=[username_validators], error_messages={'unique': _("A user with that username already exist")}, help_text=_('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),)
    type = models.CharField(_('user type'),max_length=100, db_index=True, default=UserTypes.seller)
    first_name = models.CharField(_("first name"), max_length=25, blank=True)
    last_name = models.CharField(_("last name"), max_length=25, blank=True)
    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)
    photo = models.ImageField(_('profile picture'),upload_to=user_photo_location, default="default_profilepic.png")
    is_staff = models.BooleanField(_("staff status"),default=False, help_text=_('Designates whether the user can log into this admin panel.'))
    is_active = models.BooleanField(_("active"), default=True, help_text=_(
            'Designates whether this user should be treated as active. '
            'set this to false this instead of deleting accounts.'
        ))

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'username']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        fullname = "{0:s} {1:s}".format(self.first_name, self.last_name)
        return fullname

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[self.email], **kwargs)

class SellerUser(CustomUser):
    pass