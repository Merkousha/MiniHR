# Generated by Django 3.2.20 on 2023-07-24 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HR', '0007_employee_user_employeeworkreport_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeeworkreport',
            name='employee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='HR.employee'),
        ),
        migrations.AlterField(
            model_name='employeeworkreport',
            name='work_date_day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HR.day'),
        ),
    ]
