# Generated by Django 3.0.4 on 2020-05-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_office', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
