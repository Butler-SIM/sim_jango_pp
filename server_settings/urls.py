"""server_settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls               import handler404, handler500, handler400, handler403
from django.conf.urls.static        import static
from django.contrib                 import admin
from django.urls                    import path, include
from rest_framework.authtoken.views import obtain_auth_token

from server_settings          import settings
from server_settings.settings import base

handler404 = 'server_settings.views.error404'
handler403 = 'server_settings.views.error403'
handler400 = 'server_settings.views.error400'
handler500 = 'server_settings.views.error500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('etc', include('etc.urls')),
]

urlpatterns += static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)