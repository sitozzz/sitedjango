from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 80)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
