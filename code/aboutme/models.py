from django.db import models

# Create your models here.
class Pages(models.Model):
	title= models.CharField(max_length=100, default="new page")
	uri= models.CharField(max_length=100, default="")
	text = models.TextField()
	text_html = models.TextField()
