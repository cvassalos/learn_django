from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image_name = models.CharField(max_length=30)
    date = models.DateField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    content = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="author")
    

class Tag(models.Model):
    caption = models.CharField(max_length=25)
    post = models.ManyToManyField(Post)