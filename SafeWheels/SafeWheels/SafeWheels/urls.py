"""SafeWheels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from safewheel.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('mudarsenha/', mudaSenha, name='mudarsenha'),
    path('esqueceusenha/', esqueceuSenha, name='esqueceusenha'),
    path('cadastrarestabelecimento', cadastroEstabelecimento, name='cadastrarE'),
    path('cadastrarusuario/', cadastroUsuario, name='cadastrarU'),
    path('detalhes/<id>', detalhesEstabelecimentos, name='detalhes'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('editarestabelecimento/<id>', editarEstabelecimento, name="editar"),
    path('delete/<id>', deletar, name="deletar"),
    path('update/<id>', updateEstabelecimento, name="update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)