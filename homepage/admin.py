from django.contrib import admin
from django.db import models
from homepage.models import Article
from homepage.models import Project


class Image(models.Model):
    image = models.ImageField()

class InlineImage(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
	inlines = [InlineImage]

admin.site.register(Article)
admin.site.register(Project, ProjectAdmin)