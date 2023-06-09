# Generated by Django 4.1.7 on 2023-03-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Prior", "0002_alter_category_options_alter_category_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="section",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="video",
            name="slug",
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
