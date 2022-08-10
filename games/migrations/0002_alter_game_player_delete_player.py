# Generated by Django 4.0.6 on 2022-08-01 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
