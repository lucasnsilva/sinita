from django.db import models


class Tarefas(models.Model):
    """Modelo das tarefas"""

    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=30, null=False)
    descricao = models.TextField('Descricao', max_length=100, null=False)
    sn_feito = models.BooleanField('Feito', default=False)


    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'tarefas'
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
