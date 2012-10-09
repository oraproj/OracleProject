from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'scripts.views.home', name='home'),
    url(r'admin/(.*)$', 'scripts.views.admin', name='admin'),
    url(r'logout/(.*)$', 'scripts.views.logoff', name='logout'),
    url(r'login/(.*)$', 'scripts.views.loginPage', name='login'),
    url(r'basic_configuration/$', 'scripts.views.basic_conf', name='userhome'),
    #url(r'research/(.*)/view$', 'scripts.views.research_view', name='research_view'),
    #url(r'research/(.*)/graph$', 'scripts.views.research_graph', name='research_graph'),
    (r'^assets/(.*)$', 'django.views.static.serve',
                       {'document_root': settings.MEDIA_ROOT}),
)
