# Generated by Django 4.0.3 on 2022-04-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_shops_additional_information_shops_brief_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='shop/'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='shop/'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='shop/'),
        ),
    ]