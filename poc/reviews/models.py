from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Company(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
        help_text=_('Should not exceed 255 characters')
    )

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class Review(models.Model):
    rating = models.IntegerField(
        choices=(
            (1, _('One')),
            (2, _('Two')),
            (3, _('Three')),
            (4, _('Four')),
            (5, _('Five')),
        ),
        verbose_name=_('Rating'),
        help_text=_('Scale from 1 to 5')
    )

    title = models.CharField(
        max_length=64,
        verbose_name=_('Title'),
        help_text=_('Should not exceed 64 characters')
    )

    summary = models.TextField(
        max_length=10000,
        verbose_name=_('Summary'),
        help_text=_('Should not exceed 10k characters')
    )

    ip_address = models.GenericIPAddressField(
        verbose_name=_('Ip address')
    )

    submission_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Submission date')
    )

    company = models.ForeignKey(
        Company,
        verbose_name=_('Company'),
        on_delete=models.PROTECT
    )

    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='reviews',
        verbose_name=_('Reviewer'),
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
