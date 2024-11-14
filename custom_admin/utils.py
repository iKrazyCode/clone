import re
from django.utils.safestring import mark_safe

def form_injection(text_html, url):
    """
    PASSAR O url PELA VIEW, USANDO O CONTEXT
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



    return mark_safe(texto)




