# Generated by Django 4.1.7 on 2023-03-28 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0005_alter_podcast_audiofile_alter_podcast_thumbnail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
    ]
