# Generated by Django 3.0.6 on 2020-07-05 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome')),
                ('url', models.CharField(max_length=512, verbose_name='URL')),
                ('img', models.CharField(max_length=512, verbose_name='URL image')),
            ],
        ),
    ]
