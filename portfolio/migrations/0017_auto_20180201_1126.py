# Generated by Django 2.0.1 on 2018-02-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20180201_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_field',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_height',
            field=models.IntegerField(null=True),
        ),
    ]
