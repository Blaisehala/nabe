# Generated by Django 4.0.5 on 2022-06-20 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ujamaa', '0003_alter_neighbourhood_neighbourhood_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='neighbourhood_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
