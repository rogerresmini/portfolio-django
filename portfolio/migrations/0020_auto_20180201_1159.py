# Generated by Django 2.0.1 on 2018-02-01 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20180201_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='height',
        ),
        migrations.RemoveField(
            model_name='project',
            name='width',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
