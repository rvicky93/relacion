from django import forms
from .models import Persona, Evento, TipoEvento
class EventoForm(forms.ModelForm):
#todos los campos de Evento
    class Meta:
        model = Evento
        fields = ('nombre', 'descripcion', 'fecha', 'personas', 'tipo')
        def __init__ (self, *args, **kwargs):
            super(EventoForm, self).__init__(*args, **kwargs)
            self.fields["personas"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["personas"].help_text = "Ingrese los actores que asistiran al evento"
            self.fields["personas"].queryset = Persona.objects.all()
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'telefono', 'direccion','correo','fecha_nacimiento',)
class TipoForm(forms.ModelForm):
    class Meta:
        model=TipoEvento
        fields=('nombre', 'descripcion',)
