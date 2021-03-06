from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=120)
    descption = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
