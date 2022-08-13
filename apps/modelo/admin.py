from django.contrib import admin
from .models import Cliente
from .models import Viaje
from .models import Avion
from .models import Aereolinea
from .models import Ciudad
from .models import Pais
from .models import Asiento
from .models import Boleto

admin.site.register(Cliente)
admin.site.register(Viaje)
admin.site.register(Avion)
admin.site.register(Aereolinea)
admin.site.register(Ciudad)
admin.site.register(Pais)
admin.site.register(Asiento)
admin.site.register(Boleto)