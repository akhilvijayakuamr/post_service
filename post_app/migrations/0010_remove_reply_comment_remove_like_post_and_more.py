# Generated by Django 5.1.1 on 2024-10-22 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0009_post_is_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='report',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
