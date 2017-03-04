from django.conf.urls import patterns, include, url
from apps.testingmongo import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.save_data, name='home'),
    url(r'^save_user$', views.save_user, name='save_user'),
    url(r'^login_setup$', views.login_setup, name='login_setup'),
    url(r'^logged_user$', views.logged_user, name='logged_user'),
    # url(r'^blog/', include('blog.urls')),
)
