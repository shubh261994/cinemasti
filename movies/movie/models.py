from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from django.utils.text import slugify

GENRE_CHOICES =(
		('action', 'Action'),
		('adventure', 'Adventure'),
		('animation', 'Animation'),
		('comedy', 'Comedy'),
		('drama', 'Drama'),
		('fantasy', 'Fantasy'),
		('historical', 'Historical'),
		('horror', 'Horror'),
		('mystery', 'Mystery'),
		('romance', 'Romance'),
		('science_fiction', 'Science Fiction'),
		('thriller', 'Thriller'),
	)

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Movie(models.Model):
	name = models.CharField(max_length = 255, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	tagline = models.CharField(max_length = 500, null = True, blank= True)
	genre = models.CharField(max_length = 100, choices = GENRE_CHOICES)
	director = models.CharField(max_length = 100)
	writer = models.CharField(max_length = 100)
	actors = models.TextField()
	outline = models.TextField()
	poster = models.ImageField(upload_to = upload_location)
	release_date = models.DateField()
	trailer = models.TextField(null= True, blank= True)
	created = models.DateTimeField( auto_now_add = True)
	updated = models.DateTimeField( auto_now = True) 

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("movies:detail", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = 'Movie'
		verbose_name_plural = 'Movies'
		ordering = ["-release_date","-created", "-updated"]