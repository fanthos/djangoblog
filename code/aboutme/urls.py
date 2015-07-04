from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from aboutme import views, settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'about.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^ftsadm/', include(admin.site.urls)),
    url(r'^blog/', views.blog),
    url(r'^blog$', views.blog),
) +	static(
	"/css/", document_root=settings.BASE_DIR+"/static/css/"
) + static(
	"/fonts/", document_root=settings.BASE_DIR+"/static/fonts/"
) + static(
	"/scripts/", document_root=settings.BASE_DIR+"/static/scripts/"
) + patterns( '',
    url(r'^', views.main),)