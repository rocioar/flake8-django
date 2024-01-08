from django.db import models


class BaseModelWithVerboseName(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'test'
        verbose_name_plural = 'tests'


class TestModelInheritedFromAbstractAndMetaWithVerboseName(BaseModelWithVerboseName):
    new_field = models.CharField(max_length=10)

    class Meta(BaseModelWithVerboseName.Meta):
        pass