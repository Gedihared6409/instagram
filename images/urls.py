from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^post/', views.post, name='post'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
