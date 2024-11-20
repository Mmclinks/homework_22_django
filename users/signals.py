from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .models import User


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # Только если пользователь только что зарегистрировался
        subject = _("Добро пожаловать на наш сайт!")
        message = _("Здравствуйте, {}!\n\nСпасибо за регистрацию на нашем сайте.".format(instance.first_name))
        recipient_list = [instance.email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
