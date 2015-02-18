from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'min.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'min_app.views.index'),
    url(r'^json_post/$', 'min_app.views.json_post'),
    url(r'^normal_post', 'min_app.views.normal_post'),
    url(r'^basic_get', 'min_app.views.basic_get'),
)
