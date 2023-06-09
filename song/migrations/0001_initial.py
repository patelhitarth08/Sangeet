# Generated by Django 4.1.6 on 2023-03-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('audioFile', models.FileField(blank=True, upload_to='')),
                ('artist', models.CharField(blank=True, max_length=255)),
                ('duration', models.TimeField(blank=True)),
                ('thumbnail', models.FileField(blank=True, default=None, upload_to='images')),
                ('languages', models.CharField(blank=True, choices=[('english', 'English'), ('hindi', 'Hindi'), ('gujarati', 'Gujarati')], default='hindi', max_length=8)),
                ('uploadDate', models.DateTimeField(auto_now_add=True)),
                ('likeCount', models.IntegerField(blank=True, default=0)),
                ('size', models.FloatField(blank=True)),
                ('type', models.CharField(choices=[('sad', 'Sad'), ('romantic', 'Romantic'), ('pop', 'Pop'), ('rap', 'Rap'), ('bhajan', 'Bhajan'), ('rock', 'Rock'), ('other', 'Other')], default='bhajan', max_length=8)),
                ('comments', models.ManyToManyField(blank=True, to='song.comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('audioFile', models.FileField(blank=True, upload_to='')),
                ('artist', models.CharField(blank=True, max_length=255)),
                ('duration', models.TimeField(blank=True)),
                ('thumbnail', models.FileField(blank=True, default=None, upload_to='images')),
                ('languages', models.CharField(blank=True, choices=[('english', 'English'), ('hindi', 'Hindi'), ('gujarati', 'Gujarati')], default='hindi', max_length=8)),
                ('uploadDate', models.DateTimeField(auto_now_add=True)),
                ('likeCount', models.IntegerField(blank=True, default=0)),
                ('size', models.FloatField(blank=True)),
                ('type', models.CharField(choices=[('scientific', 'Scientific'), ('geopolitics', 'Geopolitics'), ('humor', 'Humor'), ('religious', 'Religious'), ('buisness', 'Buisness'), ('historical', 'Historical'), ('interview', 'Interview')], max_length=11)),
                ('comments', models.ManyToManyField(blank=True, to='song.comment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
