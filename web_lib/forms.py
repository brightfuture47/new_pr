from cProfile import label
from django import forms
from django.forms import fields, widgets
from .models import Book

class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label="Author UUID", required= False)

class PostAuthors(forms.Form):
    name = forms.CharField(label ="Name", max_length=150, required= False)
    age = forms.IntegerField(label="Age", required= False)
    email = forms.EmailField(label="Email", required= False)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels ={
            "title": "Название книги",
            "description": "Описание книги",
            "page_num": "Количество страниц",
            "author": "Выберете автора"
        }
        widgets = {"description": widgets.TextInput}
            

