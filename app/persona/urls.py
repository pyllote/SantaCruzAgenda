from django.urls import path
from app.persona.views import PersonListApiView

urlpatterns = [
    path('api/persona/list',PersonListApiView.as_view(),name='personas')
]