# Generated by Django 5.1 on 2024-09-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_topic_level_alter_topic_lft_alter_topic_rght_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='topic',
        ),
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
    ]
