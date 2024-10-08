# Generated by Django 5.1 on 2024-09-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
