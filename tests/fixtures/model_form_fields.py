from django import models

class User(models.ModelForm):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        model = User
        fields = ('name',)

        def test_method_doesnt_error(self):
            pass
