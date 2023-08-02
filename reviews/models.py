from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Reviews(models.Model):
    """
    A model to represents service reviews provide by users.
    This model allows the application to store and manaage
    user-submitted service reviews, such as review title, content,
    rating and images.
    """

    class Meta:
        verbose_name_plural = 'Reviews'

    review_title = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    featured_image = models.ImageField(blank=True, upload_to='review-images')
    created_on = models.DateTimeField(auto_now_add=True)
    service_review = models.TextField(null=True, max_length=400)
    service_rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])  # noqa
    approved = models.BooleanField(default=False)
    carousel_review = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reviews')
