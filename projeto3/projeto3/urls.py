
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from livros.views import AutorViewSet, LivroViewSet


# Rotas da API
router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)


# Página inicial
def home(request):
    return HttpResponse("""
        <h1>API de Livros</h1>
        <p>Bem-vindo ao projeto!</p>
        <ul>
            <li><a href="/api/">API</a></li>
            <li><a href="/api/docs/">Documentação Swagger</a></li>
            <li><a href="/api/redoc/">Documentação ReDoc</a></li>
            <li><a href="/admin/">Painel Administrativo</a></li>
        </ul>
    """)


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]
