# Generated by Django 4.1.6 on 2023-03-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_remove_job_image_job_slug_job_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Website', models.URLField()),
                ('CV', models.FileField(upload_to='apply/')),
                ('Cover_Litter', models.TextField(max_length=500)),
            ],
        ),
    ]