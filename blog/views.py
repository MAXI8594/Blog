from django.shortcuts import render , get_object_or_404
from .models import Post

# Create your views here.
def render_posts(request):
    posts = Post.objects.all()
    return render (request , 'post.html' ,{ 'posts': post })

def post_detail(request ,post_id):
    posts =get_object_or_404(Post , pk=post_id)
    return render (request ,'post_details.html', {'post': post_id} )