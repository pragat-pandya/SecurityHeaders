# Generated by Django 4.1.3 on 2022-11-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0003_scan_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='host_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
