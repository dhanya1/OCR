from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)    
    image = models.ImageField(default = '')
