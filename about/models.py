from django.db import models
# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content=models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title

    





