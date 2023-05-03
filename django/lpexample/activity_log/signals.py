from django.contrib.auth.signals import user_logged_in, user_login_failed , user_logged_out
from django.dispatch import receiver

from .constants import LOGIN, LOGIN_FAILED
from .models import ActivityLog
from .utils import get_client_ip


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    message = f"{user.username} is logged in with ip:{get_client_ip(request)}"
    ActivityLog.objects.create(actor=user, action_type=LOGIN, remarks=message)


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    message = f"Login Attempt Failed for number {credentials.get('email')} with ip: {get_client_ip(request)}"
    ActivityLog.objects.create(action_type=LOGIN_FAILED, remarks=message)


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print('user logged out')