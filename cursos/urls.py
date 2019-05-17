from django.conf.urls import url,re_path
from django.urls import path,include
from cursos import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'cursos/',views.HomeCursosView.as_view(),name="cursos"),
    url(r'curso/create/$',views.CursoCreate.as_view(success_url='/cursos/'),name="curso_create"),
    url(r'curso/(?P<pk>\d+)/update/$',views.CursoUpdate.as_view(success_url='/cursos/'),name="curso_update"),
    url(r'curso/(?P<pk>\d+)/delete/$',views.CursoDelete.as_view(success_url='/cursos/'),name="curso_delete"),
    re_path(r'^curso/(?P<sigla>ICF[0-9]{3})/$', views.DetalleCursoView.as_view(),name="detalle"),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls'))
]
