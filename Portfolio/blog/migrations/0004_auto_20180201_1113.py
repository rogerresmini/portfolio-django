# Generated by Django 2.0.1 on 2018-02-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field=100, null=True, upload_to='media', width_field=100),
        ),
    ]
