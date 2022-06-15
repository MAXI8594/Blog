from django.urls import path
from . import views
from .views import render_posts , post_detail 

app_name= 'blog'

urlpatterns = [
    path("", render_posts , name='post'),
    path("<int:post_id>", post_detail ,name='post_details'),]





