from django.contrib import admin
from django.db import models
from homepage.models import Article
from homepage.models import Project
from PIL import Image


class ImageInline(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    file_path = [ImageInline]


class ArticleAdmin(admin.ModelAdmin):
	change_form_template = 'homepage/admin/change_form.html'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Project, ProjectAdmin)