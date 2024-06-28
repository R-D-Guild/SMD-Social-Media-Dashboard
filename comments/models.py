from django.db import models

# Create your models here.
from django.db import models

class Comment(models.Model):
    text = models.TextField()
    ai_review_score = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:50]
