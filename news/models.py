from django.db import models

class News(models.Model):
	title = models.CharField(max_length=255)
	url = models.URLField()
	source = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'News'
	def __str__(self):
		return self.title
