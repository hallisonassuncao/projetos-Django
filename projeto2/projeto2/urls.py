from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("API de Cadastro de Pessoas funcionando!")


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('cadpessoas.urls')),
    path('', include('cadpessoas.urls')),
]