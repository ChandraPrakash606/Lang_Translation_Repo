from django.db import models

# Create your models here.

class Translation(models.Model):
    source_language = models.CharField(max_length=10)
    target_language = models.CharField(max_length=10)
    source_text = models.TextField()
    translated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

