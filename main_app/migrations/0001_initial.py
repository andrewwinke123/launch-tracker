# Generated by Django 4.2.1 on 2023-05-31 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('mfg', models.TextField(max_length=50)),
                ('size', models.IntegerField()),
                ('orbit', models.CharField(max_length=50)),
                ('crew', models.IntegerField()),
                ('payload', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('date', models.CharField()),
            ],
        ),
    ]