# Generated by Django 2.2 on 2020-12-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boring_app', '0023_auto_20201202_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='privacy',
            field=models.IntegerField(default=None, null=True),
        ),
    ]