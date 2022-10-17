from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.title
# order according to the completed attribute. complete items sent to bottom of list. order it by the complete attriblute.
    class meta: 
        ordering = [ 'complete']





