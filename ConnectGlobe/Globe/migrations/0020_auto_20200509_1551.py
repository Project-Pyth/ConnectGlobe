# Generated by Django 3.0.4 on 2020-05-09 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Globe', '0019_auto_20200508_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='parent',
        ),
        migrations.AddField(
            model_name='postcomment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='Globe.PostComment'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='comment',
            field=models.TextField(max_length=100),
        ),
    ]
