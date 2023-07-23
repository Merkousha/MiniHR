# Generated by Django 4.2.3 on 2023-07-23 09:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0005_employeeworkreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeworkreport',
            name='work_date',
        ),
        migrations.AddField(
            model_name='employeeworkreport',
            name='work_date_day',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AddField(
            model_name='employeeworkreport',
            name='work_date_month',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HR.month'),
        ),
        migrations.AddField(
            model_name='employeeworkreport',
            name='work_date_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HR.year'),
        ),
        migrations.AlterField(
            model_name='employeeworkreport',
            name='work_type',
            field=models.CharField(choices=[('ON_SITE', 'ON_SITE'), ('REMOTE', 'REMOTE')], max_length=50),
        ),
    ]