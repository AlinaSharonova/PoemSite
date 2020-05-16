from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms, Form, EmailField, CharField

from basis.models import User


class CreativeUserForm(UserCreationForm):
    birth_date = forms.DateField(required=False, input_formats=['%Y-%m-%d', '%m/%d/%Y',
                                                                '%m/%d/%y', '%d.%m.%Y'])

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'email', 'birth_date', 'photo', 'info',
                  'birth_date')


class CreativeUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('photo', 'info', 'birth_date')


class PasswordResetRequestForm(Form):
    email = EmailField(label="Email", max_length=254)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Send email'))
        self.helper.form_method = 'post'


class PasswordResetForm(Form):
    password = CharField(label="New Password", max_length=254, widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_method = 'post'