from django.contrib import admin
from conta import models
# Register your models here.

admin.site.register(models.Conta)
admin.site.register(models.Cliente)
admin.site.register(models.RegistroBancario)