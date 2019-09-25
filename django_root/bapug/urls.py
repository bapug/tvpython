from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = [
    path('', TemplateView.as_view(template_name="homepage.html"), name="home"),
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns