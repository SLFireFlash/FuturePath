# Generated by Django 3.2.16 on 2023-02-08 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.AddField(
            model_name='company',
            name='company',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL),
        ),
    ]
