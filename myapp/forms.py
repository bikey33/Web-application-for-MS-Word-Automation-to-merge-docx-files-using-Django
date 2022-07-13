from django import forms
from .models import Mydocument
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Mydocument
        fields =('file1','file2','file3')