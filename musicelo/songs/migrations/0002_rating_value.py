# Generated by Django 5.0 on 2023-12-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='value',
            field=models.FloatField(default=1500),
        ),
    ]
