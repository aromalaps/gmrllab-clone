# Generated by Django 5.0.2 on 2024-03-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frondpage', '0003_remove_gallery_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='address',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branches',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
