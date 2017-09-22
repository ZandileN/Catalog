from django.conf.urls import url, include 
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from catalog import views 

#defines the sit url-to-view mappings. While this could contain all the url mapping code,
#it is more common to delegate some of the mapping to particular applications as you see later...


urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^catalog/', views.index, name='index'),
        
        #url(r'^catalog', 'catalog.views.index', name='index'),
        #url(r'^catalog/', include ('catalog.urls')),
        #url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += (url(r'^catalog/', include ('catalog')),)
    
#urlpatterns+= (url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
