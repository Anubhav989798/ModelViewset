# Generated by Django 3.2.18 on 2023-04-30 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_anubhav_postmodel_anubhav_gupta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='Title',
        ),
    ]
