# Generated by Django 2.0.2 on 2018-03-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='settings.MEDIA_ROOT/default_user.jpg', upload_to=''),
        ),
    ]
