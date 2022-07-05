
from xml.etree.ElementInclude import include
import django
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views
from blog.views import  PostList , PostCreate, PostUpdate ,PostDetail ,PostDelete, login_request, register_request 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name='home'),
    path('blog/', include('blog.urls')),
    path('post/list/', PostList.as_view() ,name='post_list'),
    path('post/<pk>', PostDetail.as_view() ,name='post_details'),
    path('post/create/', PostCreate.as_view() ,name='post_create'),
    path('post/update/<pk>', PostUpdate.as_view() ,name='post_update'),
    path('post/delete/<pk>', PostDelete.as_view(), name='post_delete'),
    path('login', login_request, name= 'login'),
    path('register', register_request , name='register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)