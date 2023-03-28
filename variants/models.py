from django.db import models


class Variant(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    discipline_name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    text = models.TextField()
    solution = models.JSONField()

    def __str__(self):
        return '{0}-{1}'.format(self.level, self.id)