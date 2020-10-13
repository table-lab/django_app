from django import forms
from.models import Use


class UsetableForm(forms.ModelForm):
    class Meta:
        model = Use
        fields = ['date', 'start', 'end', 'labo', 'name']
