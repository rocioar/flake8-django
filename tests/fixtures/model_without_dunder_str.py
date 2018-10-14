from django import models
from django.models import Model


class TestModel1(models.Model):
    new_field = models.CharField(max_length=10)

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2


class TestModel2(Model):
    new_field = models.CharField(max_length=10)

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2
