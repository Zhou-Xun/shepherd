# Generated by Django 3.1.5 on 2021-03-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20210326_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='img/', verbose_name='picture'),
        ),
    ]
