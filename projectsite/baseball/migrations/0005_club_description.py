# Generated by Django 3.2.16 on 2022-11-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0004_club_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
