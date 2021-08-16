from django import forms
from augapp.models import Books,Author

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name','price']


class AuthorForm(forms.ModelForm):
    class Meta:
        model= Author
        fields =['name']