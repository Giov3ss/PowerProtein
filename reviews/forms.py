from django import forms
from .models import Reviews
from .widgets import CustomClearableFileInput


class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('review_title', 'service_review', 'service_rating', 'featured_image')

    featured_image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    