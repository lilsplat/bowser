from django.conf.urls import patterns, include, url
from django.contrib import admin
#import autocomplete_light
from courses import views
#autocomplete_light.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bowser.views.home', name='home'),
    # url(r'^bowser/', include('bowser.urls')),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
	url(r'^$', 'courses.views.index', name='index'),    
	# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^autocomplete/', include('autocomplete_light.urls')),
	url(r'^courses/', include('courses.urls')),
)
