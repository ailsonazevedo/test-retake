from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Process(Base):
    number = models.CharField(max_length=1000)
    grade = models.CharField(max_length=1000)
    
# Create your models here.
