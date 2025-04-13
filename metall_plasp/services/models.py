from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class ModelService(models.Model):
	titel = models.CharField(max_length=255)
	photo = models.ImageField(upload_to="photos=/%Y/%m/%d")
	content = models.TextField(blank=True)
	category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True)


