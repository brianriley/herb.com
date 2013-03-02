from django import forms


class UploadForm(forms.Form):
    history = forms.FileField()
