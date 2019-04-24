from django import models
from django.models import Model


class TestModel1(Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'test model'
        verbose_name_plural = 'test models'

    def __str__(self):
        return self.new_field

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2


class TestModel2(models.Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'test model'
        verbose_name_plural = 'test models'

    def __str__(self):
        return self.new_field

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2
