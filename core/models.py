from django.db import models


class Image(models.Model):
    src = models.ImageField()
    alt = models.CharField(max_length=180)


class BaseImage(models.Model):
    src = models.ImageField()
    alt = models.CharField(max_length=180)

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
