# Generated by Django 3.1.4 on 2021-05-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210506_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadpicturemodel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='PoshanVatikaPics/'),
        ),
        migrations.AlterField(
            model_name='uploadwellpicturemodel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='WellPics/'),
        ),
    ]