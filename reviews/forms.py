from django import forms
from .models import Reviews
from .widgets import CustomClearableFileInput
from django.utils.html import format_html


class ReviewsForm(forms.ModelForm):
    """
    A form used to handle the creation and editiing of service review.
    It is associated with the 'Reviews' model.
    """
    class Meta:
        model = Reviews
        fields = ('review_title', 'service_review', 'service_rating', 'featured_image')  # noqa

    featured_image = forms.ImageField(
        label='Image', required=False, 
        widget=CustomClearableFileInput,
    )
    service_rating = forms.ChoiceField(
        label='Service Rating',
        choices=[(i, str(i)) for i in range (1, 6)],
        widget=forms.Select(attrs={'class': 'review-rating-dropdown'}),
    )
