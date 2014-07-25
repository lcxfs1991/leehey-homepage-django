from django.db import models

class Article(models.Model):
	main_title = models.CharField(max_length=256)
	sub_title = models.CharField(max_length=256)
	content = models.TextField()
	created_date = models.DateTimeField('date published')

class Project(models.Model):
	project_name = models.CharField(max_length=512)
	project_des = models.TextField()
	pic_path = models.CharField(max_length=512)
	pic_file = models.CharField(max_length=512)

