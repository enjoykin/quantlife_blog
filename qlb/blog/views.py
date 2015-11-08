from django.shortcuts import redirect, render
from django.http import HttpResponse
from blog.models import BlogPost

# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def index(request):
    if request.method == 'POST':
        BlogPost.objects.create(body=request.POST['item_text'])
        return redirect('/')

    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'items': posts})
