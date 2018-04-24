from django.db import models
# from django.utils import timezone


class Post(models.Model):
    word = models.CharField(max_length=256)
    description = models.TextField()

    # def publish(self):
    #     self.save()

    # def __str__(self):
    #     return self.post
