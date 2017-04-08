from django.conf.urls import patterns, include, url
from apps.testingmongo import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^graphs$', views.graphs, name='graphs'),
    url(r'^result$', views.generate_graph, name='generate_graph'),
    url(r'^geocoding$', views.geocoding, name='geocoding'),
    # url(r'^blog/', include('blog.urls')),
)
