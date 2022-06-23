from django import forms
from .models import Authors, Books


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['full_name', 'country', 'books']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-row'}),
            'country': forms.TextInput(attrs={'class': 'form-row'})
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-row'}),
            'desc': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }