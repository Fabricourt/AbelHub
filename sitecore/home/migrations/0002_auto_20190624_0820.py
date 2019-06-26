# Generated by Django 2.2 on 2019-06-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header_carousel_pics',
            old_name='motivational_statement',
            new_name='home_header_1_statement1',
        ),
        migrations.RemoveField(
            model_name='header_carousel_pics',
            name='home_header_3',
        ),
        migrations.RemoveField(
            model_name='header_carousel_pics',
            name='logo_short_name',
        ),
        migrations.AddField(
            model_name='header_carousel_pics',
            name='home_header_1_statement2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='header_carousel_pics',
            name='home_header_1_statement3',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='header_carousel_pics',
            name='home_header_2_statement1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='header_carousel_pics',
            name='home_header_2_statement2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='header_carousel_pics',
            name='home_header_2_statement3',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='header_carousel_pics',
            name='home_header_statement1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='header_carousel_pics',
            name='home_header_statement2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='header_carousel_pics',
            name='home_header_statement3',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
