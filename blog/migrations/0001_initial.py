# Generated by Django 4.2 on 2023-05-09 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("username", models.CharField(max_length=200)),
                ("password", models.CharField(max_length=200)),
                ("date_of_birth", models.DateTimeField(verbose_name="")),
                ("profile_picture", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
                ("blog_photo", models.CharField(max_length=500)),
                ("published_at", models.DateTimeField(verbose_name="date published")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.user"
                    ),
                ),
            ],
        ),
    ]