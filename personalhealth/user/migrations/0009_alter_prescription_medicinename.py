# Generated by Django 3.2.2 on 2021-06-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='medicinename',
            field=models.FileField(upload_to=''),
        ),
    ]
