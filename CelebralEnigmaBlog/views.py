from django.shortcuts import render,redirect
from .models import Post,Category
from django.urls import reverse

# Create your views here.
def home(request):
    context = {
        "categories": Category.objects.all(),
        "posts": Post.objects.all().order_by('-date'),
        "topposts":Post.objects.all().order_by('-views')[:5]
    }
    return render(request, "home.html",context)

def post(request,title):
    p = Post.objects.get(title=title)
    context = {
        "title":p.title,
        "content":p.content,
        "date":p.date,
        "categoryPosts":Category.objects.filter(posts=p).first().posts.all(),
    }
    return render(request, "post.html",context)

def write(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    
    if title or content:
        context = {
            "title": title,
            "content": content,
            "repeat": True,
            "categories": Category.objects.all()
        }
        return render(request, "write.html", context)
    
    context = {
        "categories": Category.objects.all()
    }
    return render(request, "write.html", context)


def addpost(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category_name = request.POST.get("category")
        if Post.objects.filter(title=title).exists():
            query_string = f"?title={title}&content={content}"
            write_url = reverse("write") + query_string
            return redirect(write_url)
        # Check if the category already exists
        category, created = Category.objects.get_or_create(name=category_name)
        
        # Create the post
        post = Post.objects.create(title=title, content=content)
        
        # If the category was just created, save it to ensure it has an ID
        if created:
            category.save()
        
        # Add the post to the category
        category.posts.add(post)
        
        return redirect("post", title=title)
    return redirect("home")


def category(request,cat):
    context = {
        "categories": Category.objects.all(),
        "posts": Category.objects.get(name=cat).posts.all(),
        "topposts":Post.objects.all().order_by('-views')[:5]
    }
    return render(request, "home.html",context)