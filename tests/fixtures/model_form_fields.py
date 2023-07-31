from django.forms import ModelForm


class User(ModelForm):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        model = User
        fields = ('name',)

        def test_method_doesnt_error(self):
            pass


class ExtendedUser(User):
    class Meta(User.Meta):
        fields = User.Meta.fields + ('email',)
