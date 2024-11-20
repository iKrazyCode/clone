from django.db import models

# Create your models here.
class ClientProduct(models.Model):
    client_id = models.CharField(verbose_name='Identificação do cliente', max_length=200)
    product = models.CharField(verbose_name='Nome do produto', max_length=200)
    response = models.TextField(verbose_name='Aqui será a resposta para essa requisição', null=True, blank=True, help_text="""{
   'ativo': True,
   'qtd_usuarios': 100,
                                }""")
    
    def __str__(self):
        return f"{self.client_id} - {self.product}"


