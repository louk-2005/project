# Generated by Django 5.1 on 2024-09-02 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_post_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='home.topic')),
            ],
        ),
    ]
