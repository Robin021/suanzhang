# Generated by Django 2.0 on 2017-12-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
