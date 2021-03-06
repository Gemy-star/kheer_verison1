# Generated by Django 3.1.2 on 2020-12-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_auto_20201209_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='cases',
            field=models.ManyToManyField(null=True, to='office.Needy', verbose_name='الحاله المستحقه'),
        ),
        migrations.AlterField(
            model_name='needy',
            name='national_id',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='رقم الهويه'),
        ),
    ]
