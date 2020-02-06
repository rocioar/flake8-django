from django import models
from django.models import Model


class TestModelWithMetaWithoutVerboseName(Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        pass

    def __str__(self):
        return self.new_field
