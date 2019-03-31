from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
   url = models.URLField('URL',max_length = 200,blank =True)
   comment = models.TextField(blank=True)
   author = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return "%s" % self.url
