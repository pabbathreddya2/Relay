# Generated by Django 3.2.4 on 2023-06-22 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tr_ars', '0008_message_retain'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='merge_semaphore',
            field=models.BooleanField(default=False, verbose_name='flag to indicate that merging is currently in progress'),
        ),
        migrations.AddField(
            model_name='message',
            name='merged_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='version_merged', to='tr_ars.message'),
        ),
    ]
