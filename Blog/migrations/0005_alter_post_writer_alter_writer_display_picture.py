# Generated by Django 4.2.5 on 2023-10-12 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_writer_post_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Posts', to='Blog.writer'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='display_picture',
            field=models.ImageField(blank=True, null=True, upload_to='user-img'),
        ),
    ]
