# Generated by Django 2.0.5 on 2018-05-28 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('g_id', models.AutoField(primary_key=True, serialize=False)),
                ('g_name', models.CharField(max_length=20)),
                ('g_create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'grade',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20, unique=True)),
                ('s_create_time', models.DateTimeField(auto_now_add=True)),
                ('s_operate_time', models.DateTimeField(auto_now_add=True)),
                ('g', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Grade')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]