from django.contrib.auth.models import User

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]  # Order companies alphabetically by name

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=255, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=255)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-posted_at"]  # Order jobs by most recently posted

    def __str__(self):
        return self.title

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-applied_at"]  # Order applications by most recently applied

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"



