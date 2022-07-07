# Generated by Django 4.0.5 on 2022-07-06 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motivation_app', '0013_delete_addedusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='motivation_app.comment'),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='child_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='child_comment',
            field=models.TextField(null=True),
        ),
    ]