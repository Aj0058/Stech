from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

app_name = 'MyApp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyApp.urls')),  # Replace 'Myapp' with the actual name of your app
 #   path('myapp/', include('Myapp.urls', namespace='Myapp')),
]
   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
