# Generated by Django 3.2.6 on 2021-08-05 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote_results', '0004_auto_20210805_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announced_lga_results',
            name='entered_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
