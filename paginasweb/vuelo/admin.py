from django.contrib import admin
from .models import Avion
from .models import Vuelo
from .models import Aeropuerto

admin.site.register(Avion)
admin.site.register(Vuelo)
admin.site.register(Aeropuerto)

# Register your models here.
