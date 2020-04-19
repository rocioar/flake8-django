from django.db import models


class StrBeforeFieldModel2(models.Model):
    random_property = 'foo'

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'tests'

    def __str__(self):
        return ''


class StrBeforeFieldModel(models.Model):
    """
    Model with __str__ before fields.
    """

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'tests'

    def __str__(self):
        return 'foobar'

    first_name = models.CharField(max_length=32)


class ManagerBeforeField(models.Model):
    """
    Model with manager before fields.
    """
    objects = 'manager'

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'tests'

    def __str__(self):
        return 'foobar'

    first_name = models.CharField(max_length=32)


class CustomMethodBeforeStr(models.Model):
    """
    Model with a custom method before __str__.
    """

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'tests'

    def my_method(self):
        pass

    def __str__(self):
        return 'foobar'


class ConstantsAreNotFields(models.Model):
    """
    Model with an assignment to a constant after __str__.
    """
    first_name = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'tests'

    def __str__(self):
        pass

    MY_CONSTANT = id(1)


class PerfectlyFine(models.Model):
    """
    Model which has everything in perfect order.
    """
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    objects = 'manager'

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'tests'

    def __str__(self):
        return 'Perfectly fine!'

    def save(self, **kwargs):
        super(PerfectlyFine, self).save(**kwargs)

    def get_absolute_url(self):
        return 'http://%s' % self

    def my_method(self):
        pass

    @property
    def random_property(self):
        return '%s' % self
