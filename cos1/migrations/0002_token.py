# Generated by Django 2.0.2 on 2018-03-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('token', models.TextField()),
            ],
        ),
    ]