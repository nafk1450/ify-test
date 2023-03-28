# Generated by Django 3.2.18 on 2023-03-20 18:23

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/content'), upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf', 'txt', 'mp4'])])),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0), django.core.validators.DecimalValidator])),
            ],
        ),
    ]
