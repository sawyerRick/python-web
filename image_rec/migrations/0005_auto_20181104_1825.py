# Generated by Django 2.1.3 on 2018-11-04 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_rec', '0004_shitmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShitModel',
        ),
        migrations.AlterModelOptions(
            name='filesmodel',
            options={'verbose_name': 'File', 'verbose_name_plural': 'Files'},
        ),
        migrations.RemoveField(
            model_name='filesmodel',
            name='name',
        ),
    ]
