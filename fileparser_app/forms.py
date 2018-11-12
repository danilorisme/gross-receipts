from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(
        label = 'File to Upload',
        widget=forms.FileInput(
            attrs = {
            'class': 'form-control-file form-control-lg'
        })
    )