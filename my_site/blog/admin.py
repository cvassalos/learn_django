from django.contrib import admin

# Register your models here.
from .models import Author, Post, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author",)
    list_filter = ("author", "tags", "date",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)