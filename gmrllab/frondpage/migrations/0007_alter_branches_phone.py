# Generated by Django 5.0.2 on 2024-03-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frondpage', '0006_alter_branches_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
