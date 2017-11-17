from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField


class Image(models.Model):
    # Author of the image, and the user hashes are credited to.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # JSON object containing any metadata stored with the image.
    metadata = JSONField(null=True, blank=True)
    # URL to the image.
    source = models.ImageField(
        upload_to='images',
        null=False,
        blank=False,
        max_length=500,
    )
    # Hashes should not be considered to be accurate.
    # It is stored simply for display in the UI.
    # Use the UserProfile methods to get an accurate
    # number of hashes for a given author.
    hashes = models.PositiveIntegerField(
        editable=False,
        default=0,
    )

    # Update the number of hashes.
    def increment_hashes(self, hash_count):
        self.hashes += hash_count
        self.save(update_fields=['hashes'])

    def __str__(self):
        return self.source.name
