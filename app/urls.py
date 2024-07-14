from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jets.views import jets_view



urlpatterns = [
    path('admin/', admin.site.urls),
        path('jets/',jets_view  ),

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
