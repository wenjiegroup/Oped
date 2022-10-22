# Generated by Django 3.2 on 2022-05-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegsub', '0002_auto_20211207_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='cookie_sequence_April',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Strand', models.CharField(max_length=2)),
                ('Spacer', models.CharField(max_length=50)),
                ('PAM', models.CharField(max_length=5)),
                ('PBS', models.CharField(max_length=50)),
                ('RT', models.CharField(max_length=50)),
                ('EditToNickDistance', models.IntegerField(null=True)),
                ('sgRNASpacer', models.CharField(max_length=50)),
                ('sgRNAPAM', models.CharField(max_length=50)),
                ('NickToNickDistance', models.IntegerField(null=True)),
                ('Efficiency', models.FloatField(null=True)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='cookie_sequence_April_index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PAM', models.CharField(max_length=5)),
                ('CUT_SIZE', models.IntegerField(null=True)),
                ('MAX_PBS', models.IntegerField(null=True)),
                ('MAX_RT', models.IntegerField(null=True)),
                ('MIN_PBS', models.IntegerField(null=True)),
                ('MIN_RT', models.IntegerField(null=True)),
                ('number_show', models.IntegerField(null=True)),
                ('MIN_DISGRNA', models.IntegerField(null=True)),
                ('HOMOLOGY', models.IntegerField(null=True)),
                ('input_sequence', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
    ]
