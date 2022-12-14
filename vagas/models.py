from django.db import models
from empresa.models import Vagas


class Tarefa(models.Model):
    choices_prioridade = (
        ('B', 'Baixa'),
        ('A', 'Alta'),
        ('U', 'Urgente')
    )
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    prioridade = models.CharField(max_length=1, choices=choices_prioridade)
    data = models.DateField()
    realizada = models.BooleanField(default=False)

    def icon(self):
        if self.prioridade == 'U':
            classe = "prioridade-vermelho"
        elif self.prioridade == 'A':
            classe = "prioridade-amarelo"
        elif self.prioridade == 'B':
            classe = "prioridade-verde"
        return classe


    def __str__(self):
        return self.titulo
    