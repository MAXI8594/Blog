from ast import If
from multiprocessing import context
from pdb import post_mortem
from django.shortcuts import render , get_object_or_404
from django.urls import reverse_lazy
from .models import Post
from django.template import loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm

# Create your views here.
def render_posts(request):
    posts = Post.objects.all()
    return render (request , 'post.html' ,{ 'posts': posts })

#def post_detail(request ,post_id):
    post =get_object_or_404(Post , pk=post_id)
    return render (request ,'post_details.html', {'post': post_id} )


class PostList(ListView):
    model= Post
    template_name= 'post.html'

class PostDetail(DetailView):
    model= Post
    template_name= 'post_details.html'

class PostCreate(CreateView):
    model= Post
    success_url= reverse_lazy('post_list')
    fields= [ 'title', 'description', 'image', 'date' ]

class PostUpdate(UpdateView):
    model= Post
    success_url= reverse_lazy('post_list')
    fields= ['title', 'description', 'image', 'date']

class PostDelete(DeleteView):
    model= Post
    success_url= reverse_lazy('post_list')

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario , password=contraseña)

            if user is not None:
                login(request, user)

                return render(request, 'post.html', {"mensaje":f'Bienvenido {usuario}'})
            
            else:

                return render(request, 'post.html', {"mensaje":'Error datos incorrectos'})
        
        else:

            return render(request, 'post.html', {"mensaje":'Error formulario erroneo'})

    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register_request(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return render(request, 'post.html', {'mensaje': f'Usuario {username} creado'})
        
    else:
        form = UserRegistrationForm()
            
    return render(request, 'register.html', {'form': form})



    
