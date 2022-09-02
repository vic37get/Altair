from django.db import models

# Create your models here.
class LicitacaoForm(models.Model):

    orgao = models.CharField(
        max_length=255,
        null=False,
        blank=False
  )

    municipio = models.CharField(
        max_length=255,
        null=False,
        blank=False
  )

    tipoObjeto = models.CharField(
        max_length=25,
        null=False,
        blank=False
  )

    objeto = models.CharField(
        max_length=255,
        null=False,
        blank=False
  )

    dataAbertura = models.DateField(
        null=False,
        blank=False
  )