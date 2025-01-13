from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.core.mail import EmailMessage

from .tasks import send_new_blog_post_email
from .models import Post, Category, EmailSubs
from .htmlStrings import html_email_template
from urllib.parse import unquote


def home(request):
    context = {
        "displayAll" : False,
        "categories": Category.objects.all(),
        "posts": Post.objects.all().order_by('-date'),
        "topposts": Post.objects.all().order_by('-views')[:5],
    }
    return render(request, "home.html", context)


def post(request, title):
    p = get_object_or_404(Post,title=unquote(title))
    catList = Category.objects.filter(posts=p).first().posts.all() if Category.objects.filter(posts=p).exists() else []
    context = {
        "title": p.title,
        "content": p.content,
        "date": p.date,
        "categoryPosts": catList,
    }
    return render(request, "post.html", context)


def write(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    description = request.GET.get("description")

    context = {
        "title": title,
        "description": description,
        "content": content,
        "repeat": bool(title or content),
        "categories": Category.objects.all(),
        "password": "sanatjha"
    }
    return render(request, "write.html", context)


def addpost(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category_name = request.POST.get("category")
        description = request.POST.get("description")
        
        if Post.objects.filter(title=title).exists():
            query_string = f"?title={title}&content={content}&description={description}"
            write_url = reverse("write") + query_string
            return redirect(write_url)
        
        category, created = Category.objects.get_or_create(name=category_name)
        post = Post.objects.create(title=title, content=content, description=description)
        
        if created:
            category.save()
        
        category.posts.add(post)

        try:
            send_new_blog_post_email(post.title, post.description, f"http://celebral-enigma.onrender.com/post/{title}", [subscriber.email for subscriber in EmailSubs.objects.all()])
        except Exception as e:
            print(f"Error sending email: {e}")
        
        return redirect("post", title=title)
    
    return redirect("home")


def category(request, cat):
    context = {
        "displayAll" : True,
        "categories": Category.objects.all(),
        "posts": get_object_or_404(Category,name=unquote(cat)).posts.all(),
        "topposts": Post.objects.all().order_by('-views')[:5]
    }
    return render(request, "home.html", context)


def increase_view_count(request):
    if request.method == 'POST':
        post_title = request.POST.get('post_title')
        post = Post.objects.get(title=post_title)
        post.views += 1
        post.save()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False}, status=400)


def newsubscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        if not EmailSubs.objects.filter(email=email).exists():
            EmailSubs.objects.create(name=name, email=email)

            email_message = EmailMessage(
                "Thanks for subscribing.",
                html_email_template.format(subscriber_name=name),
                "sanatjha4@gmail.com",
                [email]
            )
            email_message.content_subtype = "html"

            try:
                email_message.send(fail_silently=False)
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)}, status=500)
        else:
            return JsonResponse({'success': False, 'error': "Already subscribed."}, status=500)
    
    return JsonResponse({'success': False}, status=400)


def unsubscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        EmailSubs.objects.get(email=email).delete()
        return JsonResponse({'success': True})
    
    if request.method == "GET":
        return render(request, "unsubscribe.html")
    
    return JsonResponse({'success': False}, status=400)
