# Generated by Django 4.1.2 on 2022-10-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_release'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='release',
            name='date',
            field=models.DateField(verbose_name='release date'),
        ),
    ]