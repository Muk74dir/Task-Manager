# Generated by Django 4.2.7 on 2023-11-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0002_rename_images_photomodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='priority',
            field=models.CharField(choices=[('3', 'Low'), ('2', 'Medium'), ('1', 'High')]),
        ),
    ]
