# Generated by Django 4.1.3 on 2022-11-24 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_siteusers_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
