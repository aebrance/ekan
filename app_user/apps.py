from django.apps import AppConfig


class AppUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_user'

    # permite usar señales asociadas a 
    def ready(self):
        import app_user.signals
