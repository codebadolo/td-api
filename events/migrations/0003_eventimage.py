# Generated by Django 5.1.7 on 2025-03-28 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_images', to='events.event')),
            ],
        ),
    ]
