from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('', include('index.urls', namespace='index')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('rosetta/', include('rosetta.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('about/', include('about.urls', namespace='about')),
    path('blog/', include('blog.urls', namespace='blog')),
)