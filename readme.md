# configuração de ambiente

máquina utilizada: Ubuntu 24.04.1 LTS x86_64 

    sudo apt install python3
    sudo apt install python3.12-venv
    
    python3 -m venv venv
    source venv/bin/activate

    pip3 install django
    pip3 install djangorestframework
    pip3 install django-cors-headers
    pip3 install django-cors
    pip3 install drf-yasg # hi swagger

    django-admin startproject ia2ecc
    cd ia2ecc

# executar a main
    python3 manage.py runserver

    python3 manage.py startapp ia2eccApp

# configurar o settings.py adicionando as seguintes configurações:

    INSTALLED_APPS = [
        'rest_framework',
        'corsheaders',
        'ia2eeccApp'
    ]

    CORS_ORIGIN_ALLOW_ALL = True

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
    ]

# configurar as models.py (classes) no app

# fazendo as migrações (database) - caso feita alguma alteração em models, basta rodar isso de novo
    python3 manage.py makemigrations ia2eccApp

# aplicando as migrações
    python3 manage.py migrate ia2eccApp

# configurar as urls.py do app primeiro

    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from .views import UserViewSet, AnimalViewSet

    # criação do router

    router = DefaultRouter()
    router.register(r'usuarios', UserViewSet, basename='usuarios')
    router.register(r'animais', AnimalViewSet, basename='animais')


    # i ncluindo as URLs geradas pelo router

    urlpatterns = [
        path('', include(router.urls)),
    ]

# configurar as urls da "main" e o swagger

    from django.contrib import admin
    from django.urls import path, include
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="API de Avaliação de Animais",
            default_version='v1',
            description="Documentação da API de Avaliação de Condição Corporal de Animais",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="suporte@exemplo.com"),
            license=openapi.License(name="MIT License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('ia2eccApp.urls')),  # Inclui as URLs da app
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

# executar a main e testar no postman
python3 manage.py runserver
