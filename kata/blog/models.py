from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """Model definition for Post."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def str(self):
        """Str representation of Post."""
        return self.title