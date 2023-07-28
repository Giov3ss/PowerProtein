from django import forms
from .models import ExpertAdvice
from django.core.exceptions import ValidationError


class ExpertAdviceAddFrom(forms.ModelForm):
    """
    Define the ExpertAdviceAddFrom form, inheriting from the Modelform class.
    """
    class Meta:
        model = ExpertAdvice
        fields = ['name', 'email', 'message']
        
        # Customize the widgets for each field to add CSS classes and attr.
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'message': forms.Textarea(attrs={'class': 'message-field'}),
    }

    # Define the clean() method to add custom from validation.
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

    # Define the __init__() method to customize the labels for each field.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Your Name'
        self.fields['email'].label = 'Your Email'
        self.fields['message'].label = 'Message'
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['message'].widget.attrs['rows'] = 4
