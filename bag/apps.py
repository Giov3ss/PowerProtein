from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    - Use BigAutoField as the default primary key
    - Setting the name of the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
