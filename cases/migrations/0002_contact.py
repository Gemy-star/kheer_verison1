# Generated by Django 3.1.4 on 2020-12-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='الأسم')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='العنوان')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='الهاتف')),
                ('message', models.TextField(blank=True, null=True, verbose_name='الرساله')),
            ],
        ),
    ]