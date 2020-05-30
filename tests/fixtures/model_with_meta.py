from django import models
from django.models import Model


class TestModelWithMeta(Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        a, b = 1
        verbose_name = 'test model'
        verbose_name_plural = 'test models'

    def __str__(self):
        return self.new_field
