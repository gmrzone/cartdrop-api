import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def pincode_validator(value):
    if not re.match(r"^\d{6}$", value):
        raise ValidationError(_(f"{value} is not a valid Pincode"))
