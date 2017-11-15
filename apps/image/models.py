from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    metadata = JSONField(null=True, blank=True)
    source = models.ImageField(
        upload_to='images',
        null=False,
        blank=False,
        max_length=500,
    )

    def __str__(self):
        return self.source.name
