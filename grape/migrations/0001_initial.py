# Generated by Django 2.0 on 2017-12-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
