
from django import template
from django.utils import timezone
import datetime


register = template.Library()


@register.simple_tag
def is_new(uploaded_at):
    now = timezone.now()
    return now - datetime.timedelta(days=7) <= uploaded_at <= now
