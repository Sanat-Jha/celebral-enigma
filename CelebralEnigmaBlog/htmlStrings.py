html_email_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You for Subscribing</title>
    <style>
        body {{
            font-family: 'Ubuntu', sans-serif;
            color: #333;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}
        .container {{
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            background-color: #000;
            color: #fff;
            padding: 20px;
            text-align: center;
        }}
        .header img {{
            width: 100px;
            height: auto;
            margin-bottom: 10px;
        }}
        .content {{
            padding: 20px;
            text-align: center;
        }}
        .content h1 {{
            color: #000;
            margin: 0 0 10px;
        }}
        .content p {{
            font-size: 16px;
            line-height: 1.5;
            margin: 0;
        }}
        .footer {{
            background-color: #f4f4f4;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: #666;
        }}
        .footer a {{
            color: #000;
            text-decoration: none;
        }}
        .footer a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://celebral-enigma.onrender.com/static/4.png" alt="Cerebral Enigma Logo">
            <h1>Thank You for Subscribing!</h1>
        </div>
        <div class="content">
            <p>Dear {subscriber_name},</p>
            <p>Thank you for subscribing to Cerebral Enigma! We’re excited to have you on board and can’t wait to keep you updated with our latest posts and insights.</p>
            <p>Stay tuned for our upcoming content and feel free to reach out if you have any questions or feedback.</p>
            <p>Best regards,<br>
            The Cerebral Enigma Team</p>
        </div>
        <div class="footer">
            <p>If you did not subscribe to our newsletter, please ignore this email.</p>
            <p><a href="https://celebral-enigma.onrender.com">Visit our website</a></p>
        </div>
    </div>
</body>
</html>
"""
new_blog_post_email_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>New Blog Post: {post_title}</title>
        <style>
            body {{
                font-family: 'Ubuntu', sans-serif;
                color: #333;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}
            .container {{
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                background-color: #fff;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                background-color: #000;
                color: #fff;
                padding: 20px;
                text-align: center;
            }}
            .header img {{
                width: 100px;
                height: auto;
                margin-bottom: 10px;
            }}
            .content {{
                padding: 20px;
                text-align: center;
            }}
            .content h1 {{
                color: #000;
                margin: 0 0 10px;
            }}
            .content p {{
                font-size: 16px;
                line-height: 1.5;
                margin: 0;
            }}
            .content a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                color: #fff;
                background-color: #000;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                transition: background-color 0.3s;
            }}
            .content a:hover {{
                background-color: #333;
            }}
            .footer {{
                background-color: #f4f4f4;
                padding: 10px;
                text-align: center;
                font-size: 14px;
                color: #666;
            }}
            .footer a {{
                color: #000;
                text-decoration: none;
            }}
            .footer a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <img src="https://celebral-enigma.onrender.com/static/4.png" alt="Cerebral Enigma Logo">
                <h1>New Blog Post Alert!</h1>
            </div>
            <div class="content">
                <h1>{post_title}</h1>
                <p>{post_description}</p>
                <a href="{post_url}">Read the Full Post</a>
            </div>
            <div class="footer">
                <p>If you no longer wish to receive these updates, please <a href="https://celebral-enigma.onrender.com/unsubscribe">unsubscribe here</a>.</p>
                <p><a href="https://celebral-enigma.onrender.com">Visit our website</a></p>
            </div>
        </div>
    </body>
    </html>
    """