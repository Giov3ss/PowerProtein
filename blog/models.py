from django.db import models
from django.contrib.auth.models import User
from products.models import Product


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Blog post model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # noqa
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = models.ImageField(blank=True, upload_to='blog-images')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    cross_sell = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product", blank=True, null=True  # noqa
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
