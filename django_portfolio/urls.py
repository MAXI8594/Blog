
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views
from blog.views import eliminarPost, postFormulario, editarPost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name='home'),
    path('blog/', include('blog.urls')),
    path('postFormulario/', postFormulario, name="postFormulario"),
    path('eliminarPost/<title>/', eliminarPost,name='eliminarPost'),
    path('editarPost/<post_title>/', editarPost ,name='editarPost'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)