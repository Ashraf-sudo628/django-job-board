# Generated by Django 4.1.6 on 2023-03-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]