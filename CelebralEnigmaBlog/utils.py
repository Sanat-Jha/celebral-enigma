import re


def remove_html_tags(text):
    # This pattern matches any text within angle brackets, including the brackets themselves
    clean = re.compile('<.*?>')
    # Replace all occurrences with an empty string
    return re.sub(clean, '', text)

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