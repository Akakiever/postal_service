# Generated by Django 4.2.4 on 2023-08-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='foreign_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('delivered', 'Delivered'), ('received', 'Received'), ('rejected', 'Rejected')], default='new', max_length=100),
        ),
    ]
