# Generated by Django 4.0.3 on 2022-09-09 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='host',
        ),
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
