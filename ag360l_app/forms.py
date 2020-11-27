from django import forms
from .models import Schedule


class BS4ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('labo', 'description', 'start_time', 'end_time',)
        widgets = {
            'labo': forms.Select(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'start_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'end_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }

    def clean_end_time(self):
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        if end_time <= start_time:
            raise forms.ValidationError(
                'The end time should be after the start time'
            )
        return end_time

