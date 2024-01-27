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
    DRUGS = 'drugs', _('Наркотики')
    CASINO = 'casino', _('Казино')
    BETTING = 'betting', _('Ставки')
    OTHER = 'other', _('Другое')


class KeywordCategory(models.TextChoices):
    EXTREMIST = 'extremist', _('Террористический ресурс')
    FRAUD = 'fraud', _('Мошенничество и фишинг')
    PORN = 'porn', _('Порно')
    ESCORT = 'escort', _('Эскорт')
    DRUGS = 'drugs', _('Наркотики')
    CASINO = 'casino', _('Казино')
    BETTING = 'betting', _('Ставки')
    CURSE = 'curse', _('Матерное слово')


class KeywordSearchPlace(models.TextChoices):
    URL = 'URL', _('URL')
    CONTENT = 'CONTENT', _('Контент')
    ALL = 'ALL', _('Все')
