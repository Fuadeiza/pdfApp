from .models import pdf_files
from django import forms
from django.core import validators

class pdf_file_form(forms.ModelForm):

    class Meta():
        model = pdf_files
        fields='__all__'