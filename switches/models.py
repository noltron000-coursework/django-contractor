from django.db import models

class Switch(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length=90)
	description = models.TextField(max_length=300)
	date_added = models.DateTimeField('date added')
