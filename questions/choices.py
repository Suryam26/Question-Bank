from django.utils.translation import gettext_lazy as _


SEMESTER_CHOICES = (
    ('ODD', _('ODD (Feb-May)')),
    ('EVEN', _('EVEN (Aug-Dec)')),
)

EXAM_CHOICES = (
    ('MST-1', _("MST-1")),
    ('MST-2', _("MST-2")),
    ('END-SEM', _("END-SEM")),
)
