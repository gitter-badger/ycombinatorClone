from django.db import models

# Create your models here.

class Forum(models.Model):
	linka = models.CharField(max_length=100, unique=False)
	linkb = models.CharField(max_length=100, unique=False)
	author = models.CharField(max_length=100, unique=False)
	title = models.CharField(max_length=100, unique=True)
	link = models.CharField(max_length=100, unique=False)
	votes= models.CharField(max_length=100, unique=False)
	time = models.TimeField(db_index=True, auto_now_add=True)
	slug = models.SlugField(max_length=100, unique=True)

	def __unicode__(self):
		return '%s' %self.title
