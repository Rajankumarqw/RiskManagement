from django.db import models


# Create your models here.
class RiskName(models.Model):
	title  = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'Risk'
		verbose_name_plural = 'Risks'
