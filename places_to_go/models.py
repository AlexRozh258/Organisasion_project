from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

static_places_storage = FileSystemStorage(
    location=os.path.join(settings.BASE_DIR, "places_to_go", "static", "places"),
    base_url="/static/places/"
)

class Place(models.Model):
    name = models.CharField(max_length=100)
    place_type = models.CharField(max_length=50, blank=True, null=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    menu = models.URLField(blank=True, null=True)
    image = models.ImageField(storage=static_places_storage, upload_to='places', blank=True, null=True)
 
    def __str__(self):
        return f"{self.name} ({self.place_type})"
