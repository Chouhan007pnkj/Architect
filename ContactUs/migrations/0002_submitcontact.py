# Generated by Django 3.1.6 on 2021-10-29 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactUs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('mobile_no', models.CharField(default='', max_length=10)),
                ('message', models.TextField(default='', max_length=500)),
            ],
        ),
    ]
