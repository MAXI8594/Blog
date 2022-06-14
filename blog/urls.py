from django.urls import path
from .views import render_post ,post_detail

  

urlpatterns = [
    path('', render_post , name='post'),
    path ('<int:post_id>' , post_detail ),

]



