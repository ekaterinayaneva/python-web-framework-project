# Generated by Django 3.1.4 on 2020-12-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]