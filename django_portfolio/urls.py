
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views
from blog.views import  PostList , PostCreate, PostUpdate ,PostDetail 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name='home'),
    path('blog/', include('blog.urls')),
    path('post/list/', PostList.as_view() ,name='post_list'),
    path('post/<pk>', PostDetail.as_view() ,name='post_details'),
    path('post/create/', PostCreate.as_view() ,name='post_create'),
    path('post/update/<pk>', PostUpdate.as_view() ,name='post_list'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)