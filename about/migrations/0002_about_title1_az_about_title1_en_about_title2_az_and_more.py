# Generated by Django 4.0.3 on 2022-05-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='title1_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title1_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title2_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title2_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
