"""
URL configuration for ppw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from app_login import views
from app_login.views import consulta_ONE, consulta_TWO, consulta_TREE, consulta_FOUR, consulta_FIVE, consulta_SIX, consulta_SEVEN, consulta_EIGTH, consulta_NINE, consulta_TEN

urlpatterns = [
    # rota, view responsavel, nome

    # path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('login', views.login, name='login'),
    # path('cadastro', views.cadastro, name='cadastro'),
    path('', views.home_page, name='home_page'),
    path('consulta-1', consulta_ONE, name='consulta-1'),
    path('consulta-2', consulta_TWO, name='consulta-2'),
    path('consulta-3', consulta_TREE, name='consulta-3'),
    path('consulta-4', consulta_FOUR, name='consulta-4'),
    path('consulta-5', consulta_FIVE, name='consulta-5'),
    path('consulta-6', consulta_SIX, name='consulta-6'),
    path('consulta-7', consulta_SEVEN, name='consulta-7'),
    path('consulta-8', consulta_EIGTH, name='consulta-8'),
    path('consulta-9', consulta_NINE, name='consulta-9'),
    path('consulta-10', consulta_TEN, name='consulta-10'),
]
