# Generated by Django 4.1.3 on 2022-11-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0005_lead_offers_alerts'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='is_deep',
            field=models.BooleanField(default=False),
        ),
    ]
