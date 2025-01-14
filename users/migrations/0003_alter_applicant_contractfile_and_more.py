# Generated by Django 4.2.13 on 2024-05-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_applicant_directionofeducation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='contractFile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='firstName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='lastName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='middleName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='passport',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='olympian',
            name='certificateImage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
