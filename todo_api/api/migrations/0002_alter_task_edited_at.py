# Generated by Django 4.2.3 on 2023-07-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='edited_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]