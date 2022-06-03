from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'


    # Lets Django know that there's a new signals
    # model with some listeners in it
    def ready(self):
        import checkout.signals
