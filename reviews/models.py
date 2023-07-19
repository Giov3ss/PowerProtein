from django.db import models
from django.urls import reverse

class Reviews(models.Model):
    """
    Model for reviews
    """

    class Meta:
        verbose_name_plural = 'Reviews'

    review_title = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    featured_image = models.ImageField(blank=True, upload_to='review-images')
    created_on = models.DateTimeField(auto_now_add=True)
    service_review = models.TextField(null=True, max_length=400)
    service_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    approved = models.BooleanField(default=False)
    carousel_review = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reviews')
