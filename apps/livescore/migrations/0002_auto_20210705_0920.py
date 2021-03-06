# Generated by Django 2.2.6 on 2021-07-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livescore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ID команды 2'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ID команды 1'),
        ),
    ]
