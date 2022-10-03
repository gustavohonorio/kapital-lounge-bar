from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name='index'),
    path('gestao/', include('gestao.urls'), name='gestao'),
]
