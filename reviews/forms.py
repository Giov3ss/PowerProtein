from django import forms
from .models import Reviews
from .widgets import CustomClearableFileInput
from django.utils.html import format_html

RATING_CHOICES = [
    (1, format_html('1 <i class="fas fa-star"></i>')),
    (2, format_html('2 <i class="fas fa-star"></i>')),
    (3, format_html('3 <i class="fas fa-star"></i>')),
    (4, format_html('4 <i class="fas fa-star"></i>')),
    (5, format_html('5 <i class="fas fa-star"></i>')),
]


class ReviewsForm(forms.ModelForm):
    """
    A form used to handle the creation and editiing of service review.
    It is associated with the 'Reviews' model.
    """
    class Meta:
        model = Reviews
        fields = ('review_title', 'service_review', 'service_rating', 'featured_image')  # noqa

    featured_image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)  # noqa
    service_rating = forms.ChoiceField(
        label='Service Rating',
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'star'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['featured_image'].label = 'Review Image'
        self.fields['featured_image'].widget.attrs['placeholder'] = 'Image:'  # noqa
        self.fields['featured_image'].widget.attrs['class'] = 'custom-file-input'  # noqa
        self.fields['featured_image'].widget.attrs['accept'] = 'image/*'  # noqa
        self.fields['featured_image'].widget.attrs['aria-describedby'] = 'filename'  # noqa
        self.fields['featured_image'].widget.attrs['onchange'] = "$('filename').text(this.files[0].name)"  # noqa
