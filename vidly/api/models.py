from django.db import models
from movies.models import Movies
from tastypie.resources import ModelResource
 
# Create your models here.

class MovieResource(ModelResource):
    class Meta:
        queryset = Movies.objects.all()
        resources_name = "movies"
