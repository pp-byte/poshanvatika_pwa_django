# Generated by Django 3.1.4 on 2021-05-22 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0018_remove_basicinformationmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinformationmodel',
            name='ifAFIF',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
