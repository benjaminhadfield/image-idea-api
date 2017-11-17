from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    coinhive_id = models.CharField(max_length=128, editable=False)

    def generate_coinhive_id(self):
        """Generates an anonymous hash from invariant user data."""
        from hashlib import sha256
        b_email = self.user.email.encode('utf-8')
        b_date_joined = self.user.date_joined.isoformat().encode('utf-8')
        return sha256(b_email + b_date_joined).hexdigest()

    def save(self, *args, **kwargs):
        self.coinhive_id = self.generate_coinhive_id()
        return super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
