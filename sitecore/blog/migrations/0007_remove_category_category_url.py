# Generated by Django 2.2 on 2019-06-23 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190623_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_url',
        ),
    ]
