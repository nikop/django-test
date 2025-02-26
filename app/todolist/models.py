from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    added = models.DateTimeField()
    modified = models.DateTimeField(null=True)
    done = models.DateTimeField(null=True)