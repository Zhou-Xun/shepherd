# Generated by Django 3.1.5 on 2021-02-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_life'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('mark', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=30)),
            ],
        ),
    ]
