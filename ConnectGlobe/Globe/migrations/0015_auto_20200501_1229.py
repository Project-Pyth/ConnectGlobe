# Generated by Django 3.0.4 on 2020-05-01 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Globe', '0014_auto_20200430_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
