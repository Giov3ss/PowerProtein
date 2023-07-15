from django import forms
from .models import ExpertAdvice

class ExpertAdviceForm(forms.ModelForm):
    class Meta:
        model = ExpertAdvice
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Your Name'
        self.fields['email'].label = 'Your Email'
        self.fields['message'].label = 'Message'
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['message'].widget.attrs['rows'] = 4
