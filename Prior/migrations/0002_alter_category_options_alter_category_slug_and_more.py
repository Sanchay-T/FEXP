# Generated by Django 4.1.7 on 2023-03-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Prior", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank="True", max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="slug",
            field=models.SlugField(blank="True", max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="section",
            name="slug",
            field=models.SlugField(blank="True", max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="video",
            name="slug",
            field=models.SlugField(blank="True", max_length=100, unique=True),
        ),
    ]
