# Generated by Django 3.2.7 on 2022-01-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignUp', '0003_auto_20220109_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_data',
            name='zip',
            field=models.CharField(default='', max_length=10),
        ),
    ]