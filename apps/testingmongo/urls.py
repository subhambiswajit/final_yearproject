from django.conf.urls import patterns, include, url
from apps.testingmongo import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'graphs^$', views.graphs, name='graphs'),
    # url(r'^blog/', include('blog.urls')),
)
