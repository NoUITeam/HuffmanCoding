# Generated by Django 3.2.9 on 2021-12-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programlist',
            name='msg',
            field=models.TextField(max_length=500),
        ),
    ]