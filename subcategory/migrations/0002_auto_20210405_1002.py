# Generated by Django 3.1.7 on 2021-04-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='catid',
            field=models.IntegerField(default='-'),
        ),
    ]