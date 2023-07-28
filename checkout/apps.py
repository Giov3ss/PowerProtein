from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    - Use BigAutoField as the default primary key
    - Setting the name of the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
