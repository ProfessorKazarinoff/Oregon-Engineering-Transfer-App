# Generated by Django 3.0.3 on 2020-08-25 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200824_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universitycourse',
            name='course_URL',
        ),
        migrations.RemoveField(
            model_name='universitycourse',
            name='course_description',
        ),
        migrations.RemoveField(
            model_name='universitycourse',
            name='course_outcomes',
        ),
        migrations.RemoveField(
            model_name='universitycourse',
            name='credits',
        ),
        migrations.RemoveField(
            model_name='universitycourse',
            name='department',
        ),
        migrations.RemoveField(
            model_name='universitycourse',
            name='pre_reqs',
        ),
    ]
