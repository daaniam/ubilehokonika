# Generated by Django 3.1.6 on 2021-02-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210219_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsettings',
            name='key',
            field=models.CharField(editable=False, max_length=48, primary_key=True, serialize=False),
        ),
    ]
