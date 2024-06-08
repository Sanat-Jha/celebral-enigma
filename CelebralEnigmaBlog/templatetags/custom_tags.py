import re
from django import template

register = template.Library()

@register.simple_tag
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
