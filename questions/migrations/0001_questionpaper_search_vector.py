# Generated by Django 3.2.4 on 2021-06-15 02:13

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', 'pg_trgm'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpaper',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]
