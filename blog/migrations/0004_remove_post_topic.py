# Generated by Django 4.2.10 on 2024-04-08 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
    ]
