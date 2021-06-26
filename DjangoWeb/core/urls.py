from django.urls import path
from .views import registro, c_actualidad, c_ciencias, c_deportes, c_negocios, c_politica, contacto, contacto_c, galeria, home, n_aceptada, n_noticias, n_rechazada, noticia_actualidad1, noticia_actualidad2, noticia_actualidad3, noticia_ciencias1, noticia_ciencias2, noticia_ciencias3, noticia_deportes1, noticia_deportes2, noticia_negocios1, noticia_negocios2, noticia_negocios3, noticia_politica1, noticia_politica2, registro, inicio, s_noticia

urlpatterns = [
    path('', home,name="Home"),
    path('Inicio/', inicio,name="Inicio"),
    path('Inicio/Registro/', registro,name="registro"),
    path('Inicio/Registro/nuevas-noticias.html',n_noticias,name="n_noticias"),
    path('Inicio/Subir-noticia',s_noticia,name="s_noticia"),
    path('Inicio/Noticia-aceptada',n_aceptada,name="n_aceptada"),
    path('Inicio/Noticia-rechazada',n_rechazada,name="n_rechazada"),
    path('Ciencias/',c_ciencias,name="Ciencias"),
    path('Ciencias/n_ciencias1',noticia_ciencias1,name="n_ciencias1"),
    path('Ciencias/n_ciencias2',noticia_ciencias2,name="n_ciencias2"),
    path('Ciencias/n_ciencias3',noticia_ciencias3,name="n_ciencias3"),
    path('Actualidad/',c_actualidad,name="Actualidad"),
    path('Actualidad/n_actualidad1',noticia_actualidad1,name="n_actualidad1"),
    path('Actualidad/n_actualidad2',noticia_actualidad2,name="n_actualidad2"),
    path('Actualidad/n_actualidad3',noticia_actualidad3,name="n_actualidad3"),
    path('Galeria/',galeria,name="Galeria"),
    path('Deportes/',c_deportes,name="Deportes"),
    path('Deportes/n_deportes1',noticia_deportes1,name="n_deportes1"),
    path('Deportes/n_deportes2',noticia_deportes2,name="n_deportes2"),
    path('Negocios/',c_negocios,name="Negocios"),
    path('Negocios/n_negocios1',noticia_negocios1,name="n_negocios1"),
    path('Negocios/n_negocios2',noticia_negocios2,name="n_negocios2"),
    path('Negocios/n_negocios3',noticia_negocios3,name="n_negocios3"),
    path('Politica/',c_politica,name="Politica"),
    path('Politica/n_politica1',noticia_politica1,name="n_politica1"),
    path('Politica/n_politica2',noticia_politica2,name="n_politica2"),
    path('Inicio/Contacto',contacto,name="Contacto"),
    path('Inicio/Contacto-success',contacto_c,name="Contacto-correcto"),

]
