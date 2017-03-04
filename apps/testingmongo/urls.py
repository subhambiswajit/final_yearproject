from django.conf.urls import patterns, include, url
from apps.testingmongo import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),
)
