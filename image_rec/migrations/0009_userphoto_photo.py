# Generated by Django 2.1.3 on 2018-11-05 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_rec', '0008_remove_userphoto_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphoto',
            name='photo',
            field=models.ImageField(default='thisismycar', upload_to='cars'),
        ),
    ]