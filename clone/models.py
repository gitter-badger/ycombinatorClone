from django.db import models

# Create your models here.

class Forum(models.Model):
	Title = models.CharField(max_length=100, unique=True)
	Link = models.CharField(max_length=100, unique=False)
	Votes= models.CharField(max_length=100, unique=False)
	Time = models.TimeField(db_index=True, auto_now_add=True)
	Slug = models.SlugField(max_length=100, unique=True)

	def __unicode__(self):
		return '%s' %self.Title
