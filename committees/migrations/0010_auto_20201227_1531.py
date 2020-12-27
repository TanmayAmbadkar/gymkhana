# Generated by Django 3.1.1 on 2020-12-27 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('committees', '0009_calendarevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CommitteeAdmin',
        ),
    ]
