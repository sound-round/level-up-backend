from django.db import models as m

class BaseModel(m.Model):
	created = m.DateTimeField(auto_now_add=True)
	updated = m.DateTimeField(auto_now=True)