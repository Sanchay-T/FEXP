from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    thumbnail = models.ImageField(upload_to="categories/%Y/%m/%d")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Course(models.Model):
    categories = models.ForeignKey(
        Category, related_name="courses", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    thumbnail = models.ImageField(upload_to="courses/thumbnails")
    sub_title = models.CharField(max_length=100)
    video_intro_url = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Section(models.Model):
    course = models.ForeignKey(
        Course, related_name="sections", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField()

    def __str__(self):
        return self.title


class Video(models.Model):
    section = models.ForeignKey(
        Section, related_name="videos", on_delete=models.CASCADE
    )
    video_url = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="lessons/photos/%Y/%m/%d")
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    position = models.IntegerField()

    def __str__(self):
        return self.title


models_to_connect = [Category, Course, Section, Video]


def pre_save_categories(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug_base = instance.title if hasattr(instance, "title") else instance.name
        instance.slug = slugify(slug_base)


for model in models_to_connect:
    pre_save.connect(pre_save_categories, sender=model)
