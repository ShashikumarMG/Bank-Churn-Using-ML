# Generated by Django 2.0.2 on 2018-03-15 02:49

from django.db import migrations, models
import static.py.funcs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='DownloadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(storage=static.py.funcs.OverwriteStorage(), upload_to='downloaded/')),
            ],
        ),
        migrations.CreateModel(
            name='Prepross',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=300)),
                ('coltype', models.CharField(max_length=300)),
                ('assvar', models.CharField(max_length=300)),
                ('missingvalues', models.CharField(max_length=300)),
                ('trainingset_size', models.IntegerField()),
                ('featscaling', models.CharField(max_length=300)),
            ],
        ),
    ]
