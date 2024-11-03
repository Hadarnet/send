# Generated by Django 5.0.2 on 2024-11-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecom', '0003_chatmessage_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='chat_audio/'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chat_images/'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='chat_video/'),
        ),
    ]