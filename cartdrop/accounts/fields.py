from django.db.models import CharField, EmailField


class LowerCaseEmailField(EmailField):
    """
    Convert email to lowercase.
    """

    def to_python(self, value):
        value = super().to_python(value)
        if isinstance(value, str):
            return value.lower()
        return value


class LowerCaseCharField(CharField):
    """
    Convert email to lowercase.
    """

    def to_python(self, value):
        value = super().to_python(value)
        if isinstance(value, str):
            return value.lower()
        return value
