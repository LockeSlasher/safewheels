from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Estabelecimentos(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE) # Nome do Proprietario 
    nomeE = models.CharField(max_length=100) # Nome do Estabelecimento
    local = models.CharField(max_length=100) # Localização
    desc = models.CharField(max_length=255, blank=True, null=True) # Descrição/Detalhamento
    horario = models.CharField(max_length=100) # Horarios de Funcionamento
    imagens = models.ImageField(null=True, blank=True, upload_to="images/") # Imagens
    rampa_para_acesso = models.BooleanField(default=False, null=True)
    barras_de_apoio = models.BooleanField(default=False, null=True)
    banheiro_adapt = models.BooleanField(default=False, null=True)
    acess_transporte = models.BooleanField(default=False, null=True)
    acess_arquit = models.BooleanField(default=False, null=True)
    acess_comunic = models.BooleanField(default=False, null=True)
    acess_digital = models.BooleanField(default=False, null=True)
    acess_instrument = models.BooleanField(default=False, null=True)
    acess_program = models.BooleanField(default=False, null=True)
    acess_metod = models.BooleanField(default=False, null=True)
    def __str__(self):
        return self.nomeE