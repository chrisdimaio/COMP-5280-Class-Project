from django.db import models
from django.utils import timezone


class Words(models.Model):
    id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    word = models.CharField(max_length=256)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.word
