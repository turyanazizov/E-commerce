# Generated by Django 4.0.3 on 2022-04-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('title1', models.CharField(max_length=100)),
                ('title2', models.CharField(max_length=100)),
                ('title3', models.CharField(max_length=100)),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
                ('content3', models.TextField()),
            ],
        ),
    ]
