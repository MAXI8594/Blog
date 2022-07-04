from multiprocessing import context
from turtle import title
from django.shortcuts import render , get_object_or_404
from .models import Post
from django.template import loader
from blog.forms import PostFormulario

# Create your views here.
def render_posts(request):
    posts = Post.objects.all()
    return render (request , 'post.html' ,{ 'posts': posts })

def post_detail(request ,post_id):
    post =get_object_or_404(Post , pk=post_id)
    return render (request ,'post_details.html', {'post': post_id} )

def postFormulario(request):
    if request.method == 'POST':
        miFormulario = PostFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        post = Post(title=informacion['title'], description=informacion['description'])
        post.save()
        return render(request, 'portfolio/home.html')
    else:
        miFormulario = PostFormulario()
        return render(request, "postFormulario.html",{ "miFormulario":miFormulario})

def eliminarPost(request, title):
    post= Post.objects.get(title=title)
    post.delete()

    posts = Post.objects.all()
    context = { "posts":posts}

    return render(request, 'post.html', context)

def editarPost(request, post_title):
    post= Post.objects.get(title=post_title)
    if request.method == 'POST':
        miFormulario = PostFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            post.title= informacion['title']
            post.description= informacion['description']
            post.save()
            posts = Post.objects.all()
            context = {"posts":posts}
            return render(request, 'post.html', context)
    else:
        miFormulario = PostFormulario(initial={"title":post.title, "description":post.description})
        return render(request, "editarPost.html", {"miFormulario":miFormulario})


  