# Generated by Django 4.1.2 on 2022-10-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_release_options_alter_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(to='main_app.actor'),
        ),
    ]