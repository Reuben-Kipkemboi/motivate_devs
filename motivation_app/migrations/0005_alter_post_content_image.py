# Generated by Django 4.0.5 on 2022-07-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motivation_app', '0004_alter_post_content_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_image',
            field=models.FileField(blank=True, null=True, upload_to='images_uploaded'),
        ),
    ]
