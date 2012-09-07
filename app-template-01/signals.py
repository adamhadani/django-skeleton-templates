from django.dispatch import receiver
from django.core.signals import request_started, request_finished
from django.contrib.auth.signals import user_logged_in