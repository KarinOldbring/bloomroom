from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Checkout
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
