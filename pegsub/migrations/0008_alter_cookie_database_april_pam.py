# Generated by Django 3.2 on 2022-05-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegsub', '0007_cookie_database_april_pam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookie_database_april',
            name='PAM',
            field=models.CharField(max_length=15),
        ),
    ]
