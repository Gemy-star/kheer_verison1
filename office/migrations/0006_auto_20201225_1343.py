# Generated by Django 3.1.4 on 2020-12-25 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_auto_20201212_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='cases',
            new_name='tamkeen',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='depend_child',
        ),
    ]
