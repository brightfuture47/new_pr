from cProfile import label
from turtle import color
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
    title = forms.CharField(label ="Name Book", max_length=150, required= False)
    color = forms.CharField(label ="Color", max_length=150, required= False)

    class Meta:
        model = Book
        fields = '__all__'
        labels ={
            "description": "Описание книги",
            "page_num": "Количество страниц",
            "author": "Выберете автора"
        }
        widgets = {"description": widgets.TextInput}
            

