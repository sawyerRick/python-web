# Generated by Django 2.1.3 on 2018-11-05 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_rec', '0010_auto_20181105_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo', models.ImageField(default='thisismycar', upload_to='cars')),
            ],
        ),
        migrations.RemoveField(
            model_name='userphoto',
            name='photo',
        ),
    ]
