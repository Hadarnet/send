# Generated by Django 5.0.2 on 2024-11-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_account_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]