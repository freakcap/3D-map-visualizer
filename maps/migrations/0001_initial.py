# Generated by Django 3.0.6 on 2020-05-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgUrl', models.CharField(max_length=300)),
            ],
        ),
    ]
