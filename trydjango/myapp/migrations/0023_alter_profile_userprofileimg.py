# Generated by Django 4.1.3 on 2023-01-16 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_profile_userprofileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userProfileImg',
            field=models.ImageField(default='blankpfp.jpg', upload_to='profile_images'),
        ),
    ]
