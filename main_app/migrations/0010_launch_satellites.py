# Generated by Django 4.2.1 on 2023-06-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_satellite_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='launch',
            name='satellites',
            field=models.ManyToManyField(to='main_app.satellite'),
        ),
    ]
