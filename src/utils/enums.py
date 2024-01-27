from django.db import models
from django.utils.translation import gettext as _


class HostRiskLevel(models.TextChoices):
    WHITELIST = 'whitelist', _('Доверенный')
    BLACKLIST = 'blacklist', _('Заблокированный')
    SUSPICIOUS = 'suspicious', _('Подозрительный')


class HostCategory(models.TextChoices):
    EXTREMIST = 'extremist', _('Террористический ресурс')
    FRAUD = 'fraud', _('Мошенничество и фишинг')
    PORN = 'porn', _('Порно')
    ESCORT = 'escort', _('Эскорт')
    OTHER = 'other', _('Другое')


class KeywordCategory(models.TextChoices):
    EXTREMIST = 'extremist', _('Террористический ресурс')
    FRAUD = 'fraud', _('Мошенничество и фишинг')
    PORN = 'porn', _('Порно')
    ESCORT = 'escort', _('Эскорт')
    CURSE = 'curse', _('Матерное слово')
