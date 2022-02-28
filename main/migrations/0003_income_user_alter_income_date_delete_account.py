# Generated by Django 4.0.2 on 2022-02-27 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
