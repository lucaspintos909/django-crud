# Generated by Django 4.0.2 on 2022-02-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('description', models.TextField(null=True, verbose_name='Descripción')),
                ('image', models.ImageField(null=True, upload_to='images/', verbose_name='Imagen')),
            ],
        ),
    ]
