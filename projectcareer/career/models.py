from django.db import models

class Disciplina(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField('Nome da Disciplina',max_length=50)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Disciplina'

class Aluno(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    nome_aluno = models.CharField('Nome do Aluno',max_length=50)
    email = models.CharField('Email',max_length=50)
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_aluno

    class Meta:
        verbose_name_plural = 'Aluno'