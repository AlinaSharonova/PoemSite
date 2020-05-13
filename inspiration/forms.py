from django import forms

from .models import Poem, CommentPoem

class PoemForm(forms.ModelForm):

    class Meta:
        model = Poem
        fields = ('author', 'title', 'text', 'image', 'day', 'month', 'year', 'category')
        #ordering = ["title"]


# class PoemFilterForm(forms.Form):
#     ordering = forms.ChoiceField(label="сортировка", required=False, choices=[["author", "автор"],
#                                                                               ["owner", "пользователь"]])

class CommentPoemForm(forms.ModelForm):

    class Meta:
        model = CommentPoem
        fields = ()
        ordering = []
