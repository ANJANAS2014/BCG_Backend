# Generated by Django 3.2.9 on 2021-11-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policydetails',
            name='date_of_purchase',
            field=models.DateField(blank=True, db_column='Date_of_Purchase', null=True),
        ),
    ]
