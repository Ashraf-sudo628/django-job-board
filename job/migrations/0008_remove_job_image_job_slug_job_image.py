# Generated by Django 4.1.6 on 2023-03-25 13:33

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Image',
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to=job.models.Image_upload),
            preserve_default=False,
        ),
    ]
