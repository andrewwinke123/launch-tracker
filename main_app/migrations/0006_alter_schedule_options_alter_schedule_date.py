# Generated by Django 4.2.1 on 2023-06-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_schedule'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(verbose_name='Schedule date'),
        ),
    ]