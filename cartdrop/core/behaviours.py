from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Timestamps(models.Model):
    created = models.DateTimeField(editable=False, db_index=True)
    updated = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class Slugable(models.Model):

    slug = models.SlugField(max_length=100, db_index=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class UUIDField(models.Model):

    uuid = models.UUIDField(unique=True, editable=False, default=uuid4, db_index=True)

    class Meta:
        abstract = True
