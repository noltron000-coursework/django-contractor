from django.db import models

class Key(models.Model):
	def __str__(self):
			return self.name
	name = models.CharField(max_length=300)
	description = models.CharField(max_length=90)
	date_added = models.DateTimeField('date added')
