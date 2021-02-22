# Generated by Django 3.1.6 on 2021-02-19 20:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210218_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globalsettings',
            name='id',
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='key',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=48, primary_key=True, serialize=False),
        ),
    ]
