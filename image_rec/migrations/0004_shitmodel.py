# Generated by Django 2.1.3 on 2018-11-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_rec', '0003_auto_20181104_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShitModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'shit',
                'verbose_name_plural': 'shit',
            },
        ),
    ]
