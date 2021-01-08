# Generated by Django 3.0.7 on 2020-12-01 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'ذكر'), ('F', 'أنثى')], max_length=1, verbose_name='النوع')),
                ('stage', models.CharField(choices=[('التمهيدى', 'التمهيدى'), ('الأبتدائى', 'الأبتدائى'), ('الأعدادى', 'الأعدادى'), ('الثانوى', 'الثانوى'), ('الجامعه', 'الجامعه')], max_length=255, verbose_name='المرحله')),
                ('age', models.SmallIntegerField(null=True, verbose_name='العمر')),
                ('enablity', models.SmallIntegerField(choices=[(1, 'مرشح للتمكين'), (2, 'غير مرشح للتمكين')], null=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='الأسم')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم الراعى')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='العنوان')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='الجوال')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='عن المؤسسه')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Needy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم الحاله')),
                ('home', models.CharField(choices=[('ملك', 'ملك'), ('إيجار', 'إيجار'), ('أخرى', 'أخرى')], max_length=255, null=True, verbose_name='السكن')),
                ('national_id', models.CharField(max_length=255, null=True, verbose_name='رقم الهويه')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='الجوال')),
                ('parent', models.CharField(max_length=255, null=True, verbose_name='العائل')),
                ('enablity', models.SmallIntegerField(choices=[(1, 'مرشح للتمكين'), (2, 'غير مرشح للتمكين')], null=True)),
                ('job', models.CharField(max_length=255, null=True, verbose_name='المهنه')),
                ('source_income', models.CharField(choices=[('راتب شهري', 'راتب شهري'), ('ضمان اجتماعي', 'ضمان اجتماعي'), ('حساب مواطن', 'حساب مواطن'), ('اخرى ', 'اخرى ')], max_length=255, null=True, verbose_name='مصدر الدخل')),
                ('health_status', models.CharField(choices=[('مريض', 'مريض'), ('حالة حرجة', 'حالة حرجة'), ('صحة جيدة', 'صحة جيدة')], max_length=255, null=True, verbose_name='الحاله الصحيه')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='الحالة الاجتماعية')),
                ('age', models.SmallIntegerField(null=True, verbose_name='العمر')),
                ('data_added', models.DateField(auto_now_add=True, null=True)),
                ('case_number', models.SmallIntegerField(blank=True, null=True)),
                ('emp_name', models.CharField(max_length=255, null=True, verbose_name='اسم المشرف')),
                ('support', models.CharField(max_length=255, null=True, verbose_name='الدعم المقدم')),
                ('department', models.CharField(max_length=255, null=True, verbose_name='المنطقة')),
                ('amount', models.CharField(max_length=255, null=True, verbose_name='قيمة الدعم')),
                ('dependencies', models.ManyToManyField(to='office.Dependency', verbose_name='الاطفال')),
            ],
        ),
        migrations.CreateModel(
            name='Foundation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم المؤسسه')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='العنوان')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='الجوال')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='عن المؤسسه')),
                ('cases', models.ManyToManyField(null=True, related_name='case', to='office.Needy', verbose_name='الحالات')),
                ('employee', models.ManyToManyField(null=True, related_name='employee', to=settings.AUTH_USER_MODEL, verbose_name='مشرفيين')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم الدوره')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='عن الدوره')),
                ('cases', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, verbose_name='الحاله المستحقه')),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office.Provider', verbose_name='الراعى')),
            ],
        ),
    ]
