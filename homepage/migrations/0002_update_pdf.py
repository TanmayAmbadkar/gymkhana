# Generated by Django 3.1.1 on 2020-12-31 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf/'),
        ),
    ]
