from django import forms
from .models import Mydocument,Bugreports
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Mydocument
        fields =('file1','file2','file3')
class BugForm(forms.ModelForm):
    class Meta:
        model = Bugreports
        fields = ('name','email','report')