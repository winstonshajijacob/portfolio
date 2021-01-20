from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    tech = models.CharField(max_length=200)
    is_code = models.BooleanField()
    is_blog = models.BooleanField()
    is_live = models.BooleanField()
    code = models.URLfield()
    blog = = models.URLfield()
    live = models.URLfield()
    is_active = is_live = models.BooleanField()
    
