# Generated by Django 5.1.2 on 2024-11-11 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MuntasirApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField(blank=True, null=True)),
                ('project_name', models.CharField(max_length=200)),
                ('duration', models.DateField(auto_now_add=True)),
                ('estimated_waste', models.FloatField(blank=True, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MuntasirApp.users')),
            ],
        ),
    ]
