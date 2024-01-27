from django.utils.translation import gettext as _
from django.db import models

from utils.enums import HostRiskLevel, KeywordCategory, HostCategory


class Host(models.Model):
    url = models.CharField(_('URL или IP адрес'), max_length=255)
    category = models.CharField(_('Категория'), max_length=20, db_index=True, choices=HostCategory.choices)
    risk_level = models.CharField(_('Уровень риска'), max_length=20, db_index=True, choices=HostRiskLevel.choices)

    def __str__(self):
        return self.url

    class Meta:
        ordering = ['-id']
        verbose_name = _('Хост')
        verbose_name_plural = _('Хосты')
        db_table = 'hosts'


class Keyword(models.Model):
    keyword = models.TextField(_('URL или IP адрес'))
    category = models.CharField(_('Категория'), max_length=20, db_index=True, choices=KeywordCategory.choices)
    allowed_for_host = models.CharField(_('Разрешен для хоста'), max_length=255, null=True)

    def __str__(self):
        return self.keyword

    class Meta:
        ordering = ['-id']
        verbose_name = _('Ключевое слово')
        verbose_name_plural = _('Ключевые слова')
        db_table = 'keywords'
