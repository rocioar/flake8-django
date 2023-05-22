from django.db import models
from django.db.models import Model


class TestModel1(models.Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'test model'
        verbose_name_plural = 'test models'

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2


class TestModel2(Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'test model'
        verbose_name_plural = 'test models'

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2


class TestModel3(Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        abstract = False

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2
