from django.db import models
from django.db.models import F
# Create your models here.

class Forum(models.Model):
	counter = models.IntegerField()
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
Forum.objects.filter(pk=1).update(counter=F('counter') + 1)

