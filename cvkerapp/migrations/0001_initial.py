# Generated by Django 5.1.5 on 2025-01-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cv_photos/')),
                ('localization', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('job_opportunity', models.TextField()),
            ],
            options={
                'verbose_name': 'CV',
                'verbose_name_plural': 'CVs',
            },
        ),
    ]
