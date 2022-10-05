from django.contrib import admin
from .models import Paslauga,Automobilis,Automobilio_modelis,Uzsakymas,Uzsakymu_eilute

# Register your models here.
class AutoAdmin(admin.ModelAdmin):
    list_display = ('valstybinis_nr', 'automobilio_modelis','klientas')



class UzsakymoEilute(admin.TabularInline):
    model =Uzsakymu_eilute
    extra=1

class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ("data", 'automobilis')
    inlines = [UzsakymoEilute]

class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('automobilio_modelis','valstybinis_nr','vin_kodas','klientas')
    list_filter = ('klientas','automobilio_modelis')
    search_fields = ('automobilio_modelis',)

class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas','kaina')

admin.site.register(Paslauga)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Automobilio_modelis)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Uzsakymu_eilute)