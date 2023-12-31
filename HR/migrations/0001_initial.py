# Generated by Django 4.2.3 on 2023-07-17 16:13

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='EmployeeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dayscount', models.DecimalField(decimal_places=2, max_digits=2)),
                ('start_day', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HR.weekday')),
                ('year', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HR.year')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('join_date', models.DateField()),
                ('is_active', models.BooleanField()),
                ('employee_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HR.employeetype')),
                ('gender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HR.gender')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_work', models.BooleanField()),
                ('month', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HR.month')),
                ('weekday', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HR.weekday')),
            ],
        ),
    ]
