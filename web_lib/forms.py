from tkinter.tix import Form
from django.forms import forms

class SearchAuthor(forms,Form):
    uuid = forms.UUIDField(label="Author UUID")