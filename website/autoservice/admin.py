from django.contrib import admin
from .models import Paslauga,Automobilis,Automobilio_modelis,Uzsakymas,Uzsakymu_eilute

# Register your models here.
class AutoAdmin(admin.ModelAdmin):
    list_display = ('valstybinis_nr', 'automobilio_modelis','klientas')

admin.site.register(Paslauga)
admin.site.register(Automobilis)
admin.site.register(Automobilio_modelis)
admin.site.register(Uzsakymas)
admin.site.register(Uzsakymu_eilute)