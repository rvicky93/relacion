from django.contrib import admin
from eventos.models import Persona, PersonaAdmin, Evento, EventoAdmin
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Evento, EventoAdmin)
