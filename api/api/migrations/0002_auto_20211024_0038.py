# Generated by Django 3.2.8 on 2021-10-24 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scream',
            name='audio_path',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='scream',
            name='video_path',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
