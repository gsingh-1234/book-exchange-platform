# Generated by Django 3.1.3 on 2020-11-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookswap', '0011_auto_20201122_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img',
            field=models.ImageField(null=True, upload_to="bookswap/media/'"),
        ),
    ]
