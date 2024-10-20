# Generated by Django 5.0.7 on 2024-10-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dark_mode', models.BooleanField(default=False)),
                ('notifications', models.BooleanField(default=True)),
                ('language', models.CharField(blank=True, max_length=20)),
                ('groups', models.ManyToManyField(blank=True, related_name='user_settings_groups', to='auth.group')),
            ],
        ),
    ]
