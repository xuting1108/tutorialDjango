from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
#A include()função permite referenciar outros URLconfs. Sempre que o Django encontra include(), 
#ele corta qualquer parte do URL correspondente até aquele ponto e envia a string restante para o 
#URLconf incluído para processamento adicional.

#A ideia por trás include()é facilitar os URLs plug-and-play. Como as enquetes estão em seu próprio 
#URLconf ( polls/urls.py), elas podem ser colocadas 
#sob “/ polls /”, ou sob “/ fun_polls /”, ou sob “/ content / polls /”, ou qualquer outra raiz do caminho, 
#e o aplicativo ainda trabalhos.