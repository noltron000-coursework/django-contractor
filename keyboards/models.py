from django.db import models

class Keyboard(models.Model):
	def __str__(self):
		return self.name
	name = models.CharField(max_length=90)
	switch = models.ForeignKey(
		'switches.Switch',
		null=True,
		on_delete=models.SET_NULL
	)
	description = models.TextField(max_length=300)
	date_added = models.DateTimeField('date added')
