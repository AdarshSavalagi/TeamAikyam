# Generated by Django 4.2.6 on 2023-12-21 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='level',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]