from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'home.html')

def index(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {
        'posts':posts
    })

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('blog:index')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm(),
                'error': 'Las contraseñas no coinciden'
            })

def signout(request):
    logout(request)
    return redirect('blog:home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                    password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrectos'
        })
        else:
            login(request, user)
            return redirect('blog:index')



def noticias(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Noticias')
    )
    return render(request,'noticias.html',{
        'posts':posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'post.html', {
        'post_detail':post
    })


def tecnologia(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
    )
    return render(request, 'tecnologia.html', {
        'posts': posts
    })

def videojuegos(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'VideoJuegos')
    )
    return render(request, 'videojuegos.html', {
        'posts': posts
    })

def acerca_de(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Acerca de mi')
    )
    return render(request, 'acerca_de.html')

