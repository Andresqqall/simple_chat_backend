# Generated by Django 4.2 on 2024-06-13 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_tread_message_thread'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-id']},
        ),
    ]
