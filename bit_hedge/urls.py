from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from bit_hedge.apps.core.views import *
from django.core.urlresolvers import reverse


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home_view, name='home'),
    url(r'^premium/$', premium, name='premium'),
    url(r'^pay_fee_view/$', pay_fee_view, name='pay_fee'),
    url(r'^presentation/$', presentation),
    url(r'^pay_fee_view_confirmed/$', pay_fee_view_confirmed, name='pay_fee_confirmed'),
    url(r'^register/$', register_view, name='register'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'core/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )


if settings.IS_TESTING:
    urlpatterns += patterns('',
        url(r'^user/(?P<username>[\w@\.+-]+)/$', 'helpers42cc.views.profile',
            name='profile')
    )
