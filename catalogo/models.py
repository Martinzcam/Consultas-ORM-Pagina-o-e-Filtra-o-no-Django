from django.db import models


class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    nome = models.CharField(max_length=150)

    desenvolvedora = models.ForeignKey(
        Desenvolvedora,
        on_delete=models.PROTECT
    )

    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nome