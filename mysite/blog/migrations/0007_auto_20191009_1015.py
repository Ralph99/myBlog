# Generated by Django 2.2.4 on 2019-10-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191009_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/%Y/%m/%d'),
        ),
    ]
