# Generated by Django 2.0.1 on 2018-02-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20180201_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
