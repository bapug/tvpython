from django.dispatch import receiver
import json
import logging

from account.signals import password_changed
from account.signals import user_sign_up_attempt, user_signed_up
from account.signals import user_login_attempt, user_logged_in

logger = logging.getLogger(__name__)


def log(user='', action='', extra=dict):
    logger.info(f"User:{user} action:{action} extra:{json.stringify(extra)}")


@receiver(user_logged_in)
def handle_user_logged_in(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_LOGGED_IN",
        extra={}
    )


@receiver(password_changed)
def handle_password_changed(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="PASSWORD_CHANGED",
        extra={}
    )


@receiver(user_login_attempt)
def handle_user_login_attempt(sender, **kwargs):
    log(
        user=None,
        action="LOGIN_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_sign_up_attempt)
def handle_user_sign_up_attempt(sender, **kwargs):
    log(
        user=None,
        action="SIGNUP_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "email": kwargs.get("email"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_signed_up)
def handle_user_signed_up(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_SIGNED_UP",
        extra={}
    )
