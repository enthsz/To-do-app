from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import IntegrityError

# Create your models here.

class CustomUser(AbstractUser):
    pass  

class Tarefa(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    titulo = models.CharField(max_length=255, null=True, unique=True)  # Campo para o título da tarefa
    completo = models.BooleanField(default=False)  # Campo para indicar se a tarefa está completa ou não
    criado = models.DateTimeField(auto_now_add=True, null=True)  # Campo para armazenar a data e hora de criação da tarefa

    def save(self, *args, **kwargs):
        if not self.pk:  # Se a instância ainda não foi salva no banco de dados
            self.titulo = self.titulo.upper()  # Converte o título para letras maiúsculas antes de salvar

        if self.completo:  # Se a tarefa está sendo marcada como completa
            self.completo = True  # Garante que o estado de 'completo' seja True

        try:
            super(Tarefa, self).save(*args, **kwargs)  # Salva a tarefa no banco de dados
        except IntegrityError:
            pass  # Se ocorrer uma exceção de integridade, não faz nada apenas deixa na propria pagina

    def __str__(self):
        return self.titulo  # Retorna o título da tarefa como representação em string da instância

    class Meta:
        verbose_name = 'Tarefa'  # Define o nome singular da classe para uso em administração
        verbose_name_plural = 'Tarefas'  # Define o nome plural da classe para uso em administração
        ordering = ['criado']  # Ordena as tarefas por data de criação
