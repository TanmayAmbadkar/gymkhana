# Generated by Django 3.1.1 on 2020-12-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0011_vicepresident'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='achievement',
            field=models.TextField(blank=True, null=True),
        ),
    ]
