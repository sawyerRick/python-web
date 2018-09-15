from django.db import models

# Create your models here.

class Comment(models.Model):
	name = models.CharField(null=True, max_length=100)
	email = models.EmailField(null=True, max_length=255)
	text = models.TextField()
	created_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.text[:20]