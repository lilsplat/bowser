from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bowser.views.home', name='home'),
    # url(r'^bowser/', include('bowser.urls')),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
    #(r'^$', index),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^create_profile/$', views.create_student_profile, name='create_profile'),
)
