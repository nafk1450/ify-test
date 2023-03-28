# Generated by Django 3.2.18 on 2023-03-23 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_content_rating'),
        ('channels', '0003_auto_20230322_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='content',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channel', to='content.content'),
        ),
    ]
