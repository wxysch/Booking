# Generated by Django 4.1.3 on 2022-11-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='best',
            field=models.BooleanField(default=False),
        ),
    ]