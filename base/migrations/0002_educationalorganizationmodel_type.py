# Generated by Django 5.0.4 on 2024-06-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalorganizationmodel',
            name='type',
            field=models.CharField(blank=True, choices=[('ВУЗ', 'ВУЗ'), ('Колледж', 'Колледж')], max_length=255),
        ),
    ]
