from django import forms

class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label="Author UUID", required= False)

class PostAuthors(forms.Form):
    name = forms.CharField(label ="Name", max_length=150, required= False)
    age = forms.IntegerField(label="Age", required= False)
    email = forms.EmailField(label="Email", required= False)