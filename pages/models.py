from django.db import models


class Entry(models.Model):
    db_id = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.text

