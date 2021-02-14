# Generated by Django 3.1.6 on 2021-02-13 16:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('51a77f6e-c550-4636-9047-8ff359a4177a'), editable=False, primary_key=True, serialize=False)),
                ('cs', models.CharField(max_length=400)),
                ('en', models.CharField(blank=True, max_length=400)),
                ('ge', models.CharField(blank=True, max_length=400)),
            ],
        ),
    ]
