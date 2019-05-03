from django import models
from django.models import Model


class AbstractTestModel1(Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return self.new_field

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2


class AbstractTestModel2(models.Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return self.new_field

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2


class AbstractTestModel3(models.Model):
    new_field = models.CharField(max_length=10)

    class Meta:
        abstract = False

    def __str__(self):
        return self.new_field

    @property
    def my_brand_new_property(self):
        return 1

    def my_beautiful_method(self):
        return 2
