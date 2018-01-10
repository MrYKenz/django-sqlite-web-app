from django.conf.urls import url
from . import views

app_name = 'gallery'

urlpatterns = [
    # regex /gallery/
    url(r'^$', views.index, name='index'),
    # regex /gallery/1/
    url(r'^(?P<group_id>[0-9]+)/$', views.info, name='info'),
    # regex /gallery/gallery_id/fave
    url(r'^(?P<group_id>[0-9]+)/fave/$', views.fave, name='fave'),
]
