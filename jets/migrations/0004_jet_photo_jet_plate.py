# Generated by Django 5.0.7 on 2024-07-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jets', '0003_brand_alter_jet_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='jet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='jets/'),
        ),
        migrations.AddField(
            model_name='jet',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
