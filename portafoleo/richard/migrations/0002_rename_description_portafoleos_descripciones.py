# Generated by Django 4.1.4 on 2022-12-12 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('richard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portafoleos',
            old_name='description',
            new_name='descripciones',
        ),
    ]
