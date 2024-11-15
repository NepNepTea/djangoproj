from django import forms


class postForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField()
    image = forms.ImageField()