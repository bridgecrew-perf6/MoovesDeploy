# Generated by Django 2.2 on 2020-11-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boring_app', '0019_auto_20201128_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='statusImage/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='imageId',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='imageId',
            field=models.IntegerField(default=None, null=True),
        ),
    ]