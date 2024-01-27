from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, editable=False, verbose_name=_('Дата создания'), null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=_('Время создания'), null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name=_('Время обновления'), null=True)

    class Meta:
        abstract = True
