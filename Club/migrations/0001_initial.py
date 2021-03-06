# Generated by Django 2.2.9 on 2020-01-24 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_title', models.CharField(max_length=255)),
                ('meeting_date', models.DateField()),
                ('meeting_time', models.TimeField()),
                ('meeting_location', models.CharField(max_length=255)),
                ('meeting_agenda', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'meetings',
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=255)),
                ('resource_type', models.CharField(max_length=255)),
                ('resource_URL', models.URLField(blank=True, null=True)),
                ('resource_date_entered', models.DateField()),
                ('resource_added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'resources',
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes_text', models.TextField()),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Club.Meeting')),
            ],
            options={
                'verbose_name_plural': 'meeting_minutes',
                'db_table': 'meeting_minutes',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=255)),
                ('event_location', models.CharField(max_length=255)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_description', models.TextField()),
                ('event_added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
