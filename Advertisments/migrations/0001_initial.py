# Generated by Django 2.2.1 on 2019-05-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertismentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameTitle', models.CharField(max_length=10)),
                ('GameUrl', models.CharField(max_length=10)),
                ('ImageUrl', models.CharField(max_length=10)),
                ('GamePlatform', models.CharField(choices=[('Android', 'Android'), ('iOS', 'iOS')], max_length=20)),
                ('GameOrientation', models.CharField(choices=[('Landscape', 'Landscape'), ('Potrait', 'Potrait')], max_length=20)),
                ('AdImage', models.ImageField(upload_to='images/')),
            ],
        ),
    ]