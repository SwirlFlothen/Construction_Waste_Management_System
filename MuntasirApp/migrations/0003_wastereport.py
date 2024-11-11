# Generated by Django 5.1.1 on 2024-11-11 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MuntasirApp', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField(blank=True, null=True)),
                ('waste_generated', models.FloatField(blank=True, null=True)),
                ('waste_recycled', models.FloatField(blank=True, null=True)),
                ('waste_disposed', models.FloatField(blank=True, null=True)),
                ('environmental_impact', models.CharField(max_length=200)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MuntasirApp.project')),
            ],
        ),
    ]
