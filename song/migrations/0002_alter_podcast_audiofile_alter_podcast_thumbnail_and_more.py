# Generated by Django 4.1.6 on 2023-03-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='audioFile',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='thumbnail',
            field=models.FileField(default=None, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='song',
            name='audioFile',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='thumbnail',
            field=models.FileField(default=None, upload_to='images'),
        ),
    ]