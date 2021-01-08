# Generated by Django 3.1.2 on 2021-01-02 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0013_auto_20201229_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(blank=True, max_length=255, null=True, verbose_name='المهنه')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='التخصص')),
                ('volunteer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المتطوع')),
            ],
        ),
    ]