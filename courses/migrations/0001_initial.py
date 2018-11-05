# Generated by Django 2.1.2 on 2018-10-24 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course_number", models.CharField(max_length=10)),
                ("course_name", models.CharField(max_length=50)),
                ("college", models.CharField(max_length=30)),
                ("department", models.CharField(max_length=100)),
                ("pre_reqs", models.CharField(max_length=50)),
                ("course_description", models.TextField()),
                ("course_outcomes", models.TextField()),
                ("course_URL", models.URLField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "added_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        )
    ]
