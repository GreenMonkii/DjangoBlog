# Generated by Django 4.2.5 on 2023-10-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
