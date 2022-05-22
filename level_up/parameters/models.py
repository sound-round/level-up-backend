from level_up.BaseModel.models import BaseModel
from django.db import models as m
from django.contrib.auth.models import User

# Create your models here.
class Parameters(BaseModel):
	user = m.OneToOneField(
		User,
		on_delete=m.CASCADE,
		null=False,
		verbose_name='user',
		related_name='params',
		)

	class_name = m.CharField(default='Rookie', max_length=50, verbose_name='class')
	experience = m.BigIntegerField(default=0, verbose_name='experince')
	level = m.IntegerField(default=1, verbose_name='level')
	attributes = m.JSONField(default=dict, verbose_name='attributes')
	skills = m.JSONField(default=dict, verbose_name='skills')

	achievements = m.JSONField(default=dict, verbose_name='achievements')

	def __str__(self):
		return f'username: {self.user.username}, class: {self.class_name}, level: {self.level}'
