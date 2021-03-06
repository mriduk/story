# Generated by Django 3.1.1 on 2020-09-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_auth', '0002_auto_20200912_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='story_to_read',
            fields=[
                ('story_id', models.IntegerField(primary_key=True, serialize=False)),
                ('story_name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('current_view', models.IntegerField(default=0)),
                ('total_read', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Story section',
                'verbose_name_plural': 'Stories',
            },
        ),
    ]
