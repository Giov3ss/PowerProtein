from django.db import models


class ExpertAdvice(models.Model):
    """
    Define the model fields
    fields: 'name', 'email', 'message', and 'created_at'
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
