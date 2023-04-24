from django.apps import AppConfig


class ActivityLogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'activity_log'


    def ready(self):
        from .signals import log_user_login,log_user_login_failed

    
