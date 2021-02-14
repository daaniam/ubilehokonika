# Generated by Django 3.1.6 on 2021-02-13 17:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='id',
            field=models.UUIDField(default=uuid.UUID('865d9efb-a5dc-4c84-86fb-2287e06f8665'), editable=False, primary_key=True, serialize=False),
        ),
    ]