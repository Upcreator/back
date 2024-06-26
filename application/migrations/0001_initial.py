# Generated by Django 5.0 on 2024-04-07 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.activitymodel')),
                ('educational_organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.educationalorganizationmodel')),
            ],
        ),
        migrations.CreateModel(
            name='StudentApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('date_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=18)),
                ('status', models.CharField(choices=[('Рассмотрение', 'Рассмотрение'), ('Отклонено', 'Отклонено'), ('Принято', 'Принято')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('educational_organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.educationalorganizationmodel')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.practicemodel')),
            ],
        ),
    ]
