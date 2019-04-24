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
