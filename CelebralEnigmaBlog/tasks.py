# myapp/tasks.py

from django.core.mail import EmailMessage
from .htmlStrings import new_blog_post_email_template

def send_new_blog_post_email(post_title, post_description, post_url, recipient_email_list):


    sender_mail = "sanatjha4@gmail.com"
    subject = f"New Blog Post: {post_title}"
    email_message = EmailMessage(
        subject,
        new_blog_post_email_template.format(
            post_title=post_title,
            post_description=post_description,
            post_url=post_url
        ),
        sender_mail,
        recipient_email_list
    )
    email_message.content_subtype = "html"
    try:
        email_message.send(fail_silently=False)
    except Exception as e:
        print(f"Error sending email: {e}")
