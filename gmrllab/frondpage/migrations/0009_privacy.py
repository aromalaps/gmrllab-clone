# Generated by Django 5.0.2 on 2024-03-25 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frondpage', '0008_our_tests_testes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
    ]
