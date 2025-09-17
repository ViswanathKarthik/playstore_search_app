from django.db import models
from django.contrib.auth.models import User


class App(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    installs = models.CharField(max_length=50, blank=True, null=True)  # keep as string for now
    size = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review of {self.app.name} by {self.user.username}"
