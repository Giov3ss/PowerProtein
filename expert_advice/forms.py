from django import forms
from .models import ExpertAdvice
from django.core.exceptions import ValidationError


class ExpertAdviceForm(forms.ModelForm):
    class Meta:
        model = ExpertAdvice
        fields = ['name', 'email', 'message']
        
        widgets = {
            'message': forms.Textarea(attrs={'class': 'message-field'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

        
        if not name:
            raise forms.ValidationError('Please enter your name.')
        if not email:
            raise forms.ValidationError('Please enter your email.')
        if not message:
            raise forms.ValidationError('Please enter your message.')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Your Name'
        self.fields['email'].label = 'Your Email'
        self.fields['message'].label = 'Message'
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['message'].widget.attrs['rows'] = 4
