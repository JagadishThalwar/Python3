from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bands/$', views.band_listing, name='band-list'),
    url(r'^bands/(\d+)/$', views.band_detail, name='band-detail'),
    url(r'^bands/search/$', views.band_search, name='band-search'),
]