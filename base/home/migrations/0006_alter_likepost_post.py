# Generated by Django 5.1 on 2024-09-02 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_post_options_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plikes', to='home.post'),
        ),
    ]
