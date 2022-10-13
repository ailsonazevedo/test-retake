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
    number = models.CharField(max_length=1000, verbose_name='Número do Processo:', unique=True)
    judicialClass = models.CharField(max_length=1000, verbose_name='Classe:')
    topic = models.CharField(max_length=1000, verbose_name='Assunto:')
    judge = models.CharField(max_length=500, verbose_name='Juiz:')
    parts = models.ManyToManyField(Parts, related_name='parts', verbose_name='Partes:')
    category = models.CharField(max_length=500, null=True, blank=True, verbose_name='Categoria:')

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['-created']
        verbose_name = 'Process'
        verbose_name_plural = 'Processes'

