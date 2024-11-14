import re
from django.utils.safestring import mark_safe

def form_injection(text_html, template_copy):
    """
    PASSAR O url PELA VIEW, USANDO O CONTEXT
    Template é a instancia do TemplateCopy
    """
    texto = text_html

    action = "{% url 'home:renderizator' url=URL %}"

    texto = re.sub(
        r'(action[ ]*=[ ]*[\'"])(.*?)([\'"][ ]*)',
        r'\1{}\3'.format(action),
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    texto = re.sub(
        r'(method[ ]*=[ ]*[\'"])(.*?)([\'"][ ]*)',
        r'\1{}\3'.format('POST'),
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    texto = re.sub(
        r'(<form.*?>)',
        r'\1{% csrf_token %}',
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    texto = re.sub(
        r'(<script.*?>)(.*?)(</script>)',
        r'',
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # src: adicionar o dominio do site no começo 
    template_copy_url_trated = re.search(r'^(https?://[^/]+/)', template_copy.url_clonar).group(0)
    template_copy_url_trated = str(template_copy_url_trated) + '/' if not str(template_copy_url_trated).endswith('/') else template_copy_url_trated

    texto = re.sub(
        r'(src[ ]*=[ ]*[\'"]?)\.?\/(.*?)([\'"][ ]*?)',
        r'\1{}\2\3'.format(template_copy_url_trated),
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )

    # href: adicionar o dominio do site no começo 
    texto = re.sub(
        r'(href[ ]*=[ ]*[\'"]?)\.?\/(.*?)([\'"][ ]*?)',
        r'\1{}\2\3'.format(template_copy_url_trated),
        texto,
        flags=re.IGNORECASE | re.DOTALL
    )



    return mark_safe(texto)




