# Generated by Django 4.1.6 on 2023-03-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_alter_podcast_audiofile_alter_podcast_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='thumbnail',
            field=models.FileField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='song',
            name='thumbnail',
            field=models.FileField(upload_to='images'),
        ),
    ]