# Generated by Django 3.1.1 on 2020-12-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20201223_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos/'),
        ),
    ]
