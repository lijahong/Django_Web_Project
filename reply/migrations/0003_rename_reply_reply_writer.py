# Generated by Django 4.0.5 on 2022-06-20 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0002_reply_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='reply',
            new_name='writer',
        ),
    ]