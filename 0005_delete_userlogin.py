# Generated by Django 5.0.3 on 2024-03-24 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_userlogin_alter_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLogin',
        ),
    ]
