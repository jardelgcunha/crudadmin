from django.contrib import admin

# Importa e registra os modelos
from app.models import Cliente

# Cria classe Admin
#class ClienteAdmin (admin.modelAdmin):
#    class Meta:
#        model = Cliente

# Registra modelo
admin.site.register(Cliente)