# Generated by Django 4.1.3 on 2022-11-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruises', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cruisephoto',
            options={'verbose_name': 'Круиз фото', 'verbose_name_plural': 'Фото круиза'},
        ),
        migrations.RenameField(
            model_name='cruisephoto',
            old_name='title',
            new_name='cruise',
        ),
        migrations.AddField(
            model_name='cruisephoto',
            name='photo',
            field=models.ImageField(default=1, upload_to='cruises/'),
            preserve_default=False,
        ),
    ]
