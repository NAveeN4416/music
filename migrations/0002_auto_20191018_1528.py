# Generated by Django 2.0.6 on 2019-10-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='dob',
            field=models.DateField(blank=True),
        ),
    ]
