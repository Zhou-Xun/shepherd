# Generated by Django 3.1.5 on 2021-03-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20210326_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='picture'),
        ),
        migrations.AlterField(
            model_name='study',
            name='content',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='study',
            name='note',
            field=models.FileField(blank=True, null=True, upload_to='notes/%Y/%m/%d/'),
        ),
    ]
