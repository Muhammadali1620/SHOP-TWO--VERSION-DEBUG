# Generated by Django 5.0.4 on 2024-04-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='featurevalue',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='featurevalue',
            name='slug',
            field=models.SlugField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='featurevalue',
            unique_together={('feature', 'slug')},
        ),
    ]
