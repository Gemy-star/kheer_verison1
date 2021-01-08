# Generated by Django 3.0.7 on 2020-12-10 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_auto_20201209_2255'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0006_remove_payment_payment_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم الشهاده')),
                ('description', models.TextField(blank=True, null=True, verbose_name='وصف')),
                ('found', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.Foundation')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
