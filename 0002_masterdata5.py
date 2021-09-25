# Generated by Django 3.2.7 on 2021-09-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masterdata5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField(verbose_name='Roll Number')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('class_name', models.CharField(max_length=100, verbose_name='Class Name')),
            ],
            options={
                'unique_together': {('roll_number', 'class_name')},
            },
        ),
    ]