from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    ##order method
    class Meta:
        ordering = ('-timestamp','title')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    num_pg = models.IntegerField()
    author = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title
class SmithBook(Book):
    authors = models.ManyToManyField(Author,limit_choices_to={'name+endswith':'Smith'})
admin.site.register(BlogPost,BlogPostAdmin)
