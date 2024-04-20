from django import forms
from notes.models import Documents 


class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['docu_title', 'docu_description', 'docu_link', 'docu_file', 'docu_image']