from django.urls import path
from app.persona.views import PersonListApiView, PersonaCreateApiView, PersonDetailView, \
    PersonDeleteView, PersonActualizarView, PersonApiLista, ReunionListApiView, ReunionApiListaLink, \
    PersonPaginationLits, ReunionByPersonJob

urlpatterns = [
    path('api/persona/list',PersonListApiView.as_view(),name='personas'),
    path('api/persona/create/', PersonaCreateApiView.as_view(),name='crearpersona'),
    path('api/persona/detalle/<int:pk>/',PersonDetailView.as_view(), name='detallepersona'),
    path('api/persona/actualizar/<int:pk>/',PersonActualizarView.as_view(), name='actualizarpersona'),
    path('api/persona/eliminar/<int:pk>/',PersonDeleteView.as_view(),name='eliminarpersona'),

    #URL para ver el funcionamiento de un serializador que no depende de un modelo
    path('api/persona/listado',PersonApiLista.as_view(),name='personaslistado'),

    #--URL para reunion
    path('api/reunion/lista',ReunionListApiView.as_view(),name='reunion'),

    #--Para el link
     path('api/reuniones-link/',ReunionApiListaLink.as_view(),),
    
    #--Url con paginación
    path('api/personas/paginacion/',PersonPaginationLits.as_view(),),

    #--Consultas especiales
     path(
        'api/reunion/por-job/',ReunionByPersonJob.as_view(),
    ),
]