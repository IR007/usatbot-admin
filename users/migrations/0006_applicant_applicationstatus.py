# Generated by Django 4.2.13 on 2024-05-15 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_applicant_languageofeducation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='applicationStatus',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('SUBMITTED', 'SUBMITTED'), ('REJECTED', 'REJECTED'), ('ACCEPTED', 'ACCEPTED'), ('PASSED', 'PASSED'), ('FAILED', 'FAILED'), ('EXAMINED', 'EXAMINED')], default='DRAFT', max_length=20),
        ),
    ]