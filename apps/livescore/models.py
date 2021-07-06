import os
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.apps import apps
from django.utils.translation import gettext_lazy as _


class Match(models.Model):
    """
        Результат
    """
    match_link = models.CharField(
        _('Ссылка'),
        max_length=255,
        blank=True, null=True,
    )
    tour = models.CharField(
        _('Стадия'),
        max_length=255,
        blank=True, null=True,
    )
    match_date = models.CharField(
        _('Дата'),
        max_length=255,
        blank=True, null=True,
    )
    match_time = models.CharField(
        _('Время'),
        max_length=255,
        blank=True, null=True,
    )
    place = models.CharField(
        _('Место проведения'),
        max_length=255,
        blank=True, null=True,
    )
    home_team_title = models.CharField(
        _('Команда 1'),
        max_length=255,
        blank=False, null=False,
    )
    away_team_title = models.CharField(
        _('Команда 2'),
        max_length=255,
        blank=False, null=False,
    )
    home_team_id = models.CharField(
        _('ID команды 1'),
        max_length=255,
        blank=True, null=True,
    )
    away_team_id = models.CharField(
        _('ID команды 2'),
        max_length=255,
        blank=True, null=True,
    )
    home_team_score_ft = models.IntegerField(
        _('Голы команды 1'),
        blank=True, null=True,
    )
    away_team_score_ft = models.IntegerField(
        _('Голы команды 2'),
        blank=True, null=True,
    )

    class Meta:
        db_table = 'livescore_match'
        verbose_name = _('Результат')
        verbose_name_plural = _('Результаты')

    def display_title(self):
        return '{} - {}'.format(self.home_team_title, self.home_team_title)

    def __str__(self):
        return '{} - {}'.format(self.home_team_title, self.home_team_title)