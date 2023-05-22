from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract = True


class TestModelInheritedFromAbstract(BaseModel):
    new_field = models.CharField(max_length=10)

    class Meta:
        pass
