import re
from django import template

register = template.Library()

@register.simple_tag
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

@register.simple_tag
def getStarter(html_code):
    # Define the regex pattern to find <p> tags
    p_tag_pattern = re.compile(r'<p>(.*?)</p>', re.DOTALL)
    
    # Find all <p> tags in the html code
    p_tags = p_tag_pattern.findall(html_code)
    
    for p_tag in p_tags:
        # Remove HTML tags from the text inside the <p> tag
        text = re.sub(r'<.*?>', '', p_tag).strip()
        if text:
            # Return the first 50 characters of the text followed by "......"
            return text[:50] + "......"
    
    return ""
