from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from django.http import HttpResponse
from django.db.models import Q
from .forms import PostForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator



def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count/2 + count %2
    first_half = all[:half]
    second_half = all[half:]

    return {'cat1': first_half, 'cat2': second_half}


def index(request):
    posts = Post.objects.all()
    # context = {"posts": posts}
    # context.update(get_categories())
    paginator = Paginator(posts,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"posts": page_obj}
    context.update(get_categories())


    return render(request, 'blog/index.html', context)

def post(request, id=None):
    posts = get_object_or_404 (Post, pk=id)
    context = {"post": posts}
    context.update(get_categories())
    return render(request, 'blog/post.html', context)

def category (request, id=None):
    c = get_object_or_404(Category, pk=id)
    posts = Post.objects.filter(category=c).order_by('-published_date')
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def search(request):
    query = request.POST.get('query')
    # posts = Post.objects.all()
    # posts = Post.objects.filter(content__icontains=query)
    posts = Post.objects.filter(Q(content__icontains=query) | Q (title__icontains=query))
    context = {"posts": posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date= datetime.now()
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect('index')

    form =PostForm()
    context = {'form':form}
    context.update(get_categories())
    return render(request, 'blog/create.html', context)






def form(request):
    return render(request, 'blog/form.html')

def show(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    email = request.POST.get('email')

    return render(request, 'blog/show.html',
                  {'name': name, 'surname': surname,
                   'age': age, 'gender': gender, 'email': email})


def access(request):
    return render(request, 'blog/access.html')

def loggedIn(request):
    admin = ["admin", "Admin", "ADMIN"]



    login = request.POST.get('login')


    if login in admin:
        greetingWord = "Administrator"
    elif login not in admin:
        greetingWord = "User"

    return render(request, 'blog/loggedin.html', {'greetingWord': greetingWord, 'login': login} )

# Create your views here.