from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import Form, EmailField, CharField, PasswordInput

from basis.models import User


class CreativeUserForm(UserCreationForm):
    birth_date = forms.DateField(required=False, input_formats=['%Y-%m-%d', '%m/%d/%Y',
                                                                '%m/%d/%y', '%d.%m.%Y'])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',
                  'email', 'birth_date', 'photo', 'info',)


class CreativeUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('photo', 'info', 'birth_date', 'first_name', 'last_name')


# class PasswordResetRequestForm(Form):
#     email = EmailField(label="Email", max_length=254)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.add_input(Submit('submit', 'Send email'))
#         self.helper.form_method = 'post'
#
#
# class PasswordResetForm(Form):
#     password = CharField(label="New Password", max_length=254, widget=PasswordInput())
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.add_input(Submit('submit', 'Save'))
#         self.helper.form_method = 'post'