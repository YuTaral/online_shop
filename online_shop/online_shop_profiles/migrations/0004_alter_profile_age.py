# Generated by Django 3.2.5 on 2021-08-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop_profiles', '0003_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
