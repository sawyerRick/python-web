from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class article(models.Model):
	def __str__(self):
		return self.title

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])


	title = models.CharField(max_length=20,null=True)
	content = models.TextField(null=True)
	pub_time = models.DateTimeField(auto_now=True)
	views = models.PositiveIntegerField(default=0)
	tag = models.CharField(max_length=20,null=True)

	