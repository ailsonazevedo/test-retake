from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Parts(Base):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

class Process(Base):
    number = models.CharField(max_length=1000)
    judicialClass = models.CharField(max_length=1000)
    topic = models.CharField(max_length=1000)
    judge = models.CharField(max_length=500)
    parts = models.ManyToManyField(Parts)
    category = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['-created']
        verbose_name = 'Process'
        verbose_name_plural = 'Processes'

