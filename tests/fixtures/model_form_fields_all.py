from django.forms import ModelForm


class User3(ModelForm):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        model = User2
        fields = '__all__'


class User4(ModelForm):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        model = User2
        fields = b'__all__'


class User5(ModelForm):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        model = User2
        fields = ['__all__']
