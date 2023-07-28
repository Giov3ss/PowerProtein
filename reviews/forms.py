from django import forms
from .models import Reviews
from .widgets import CustomClearableFileInput

RATING_CHOICES = [
    (1, '1 Star'),
    (2, '2 Stars'),
    (3, '3 Stars'),
    (4, '4 Stars'),
    (5, '5 Stars'),
]


class ReviewsForm(forms.ModelForm):
    """
    A form used to handle the creation and editiing of service review.
    It is associated with the 'Reviews' model.
    """
    class Meta:
        model = Reviews
        fields = ('review_title', 'service_review', 'service_rating', 'featured_image')

    featured_image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    service_rating = forms.ChoiceField(
        label='Service Rating',
        choices=RATING_CHOICES,
        widget=forms.Select,
    )
    