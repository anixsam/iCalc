# Generated by Django 4.0.2 on 2022-02-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_income_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(),
        ),
    ]
