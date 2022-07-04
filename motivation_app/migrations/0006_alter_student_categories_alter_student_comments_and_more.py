# Generated by Django 4.0.5 on 2022-07-04 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motivation_app', '0005_student_categories_student_comments_student_posts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='motivation_app.category'),
        ),
        migrations.AlterField(
            model_name='student',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='motivation_app.comment'),
        ),
        migrations.AlterField(
            model_name='student',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='motivation_app.post'),
        ),
        migrations.AlterField(
            model_name='student',
            name='wishlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='motivation_app.wishlist'),
        ),
    ]
