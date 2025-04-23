from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

