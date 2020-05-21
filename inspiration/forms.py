from django import forms
from django.contrib.auth.models import User

from .models import Poem, CommentPoem

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'email')
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']
#
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')

# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('date_of_birth', 'photo')

class PoemForm(forms.ModelForm):

    class Meta:
        model = Poem
        exclude = ['owner', "published_date"]
        fields = ('author', 'title', 'text', 'image', 'day', 'month', 'year', 'category')
        #ordering = ["title"]


# class PoemFilterForm(forms.Form):
#     ordering = forms.ChoiceField(label="сортировка", required=False, choices=[["author", "автор"],
#                                                                               ["owner", "пользователь"]])

class CommentPoemForm(forms.ModelForm):

    class Meta:
        model = CommentPoem
        fields = ('text',)
        ordering = ['-created', ]