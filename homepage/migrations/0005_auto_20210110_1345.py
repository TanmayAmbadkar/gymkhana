# Generated by Django 3.1.1 on 2021-01-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20210109_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='youtube',
        ),
        migrations.AddField(
            model_name='update',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
