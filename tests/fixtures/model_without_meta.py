from django import models
from django.models import Model


class TestModelWithoutMeta(Model):
    new_field = models.CharField(max_length=10)
    
    def __str__(self):
        return self.new_field
