# Generated by Django 4.2.5 on 2023-10-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_post_writer_alter_writer_display_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]