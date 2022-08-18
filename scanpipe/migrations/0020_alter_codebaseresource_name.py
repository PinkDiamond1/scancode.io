# Generated by Django 4.0.6 on 2022-08-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanpipe', '0019_auto_20220804_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codebaseresource',
            name='name',
            field=models.CharField(blank=True, help_text='File or directory name of this resource with its extension.', max_length=255),
        ),
    ]