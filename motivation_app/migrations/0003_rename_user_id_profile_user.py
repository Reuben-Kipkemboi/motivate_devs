# Generated by Django 4.0.5 on 2022-07-02 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motivation_app', '0002_student_staff_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]