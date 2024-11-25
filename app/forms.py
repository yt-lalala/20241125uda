from django import forms
from .models import UploadImage, UploadImageUra

class UploadForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)

    class Meta:
        model = UploadImage
        fields = ['image']

        
class UploadFormUra(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)

    class Meta:
        model = UploadImageUra
        fields = ['image']