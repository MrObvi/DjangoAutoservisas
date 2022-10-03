from django.db import models


# Create your models here.
class Paslauga(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=200, blank=True, help_text="Paslaugos pavadinimas")
    kaina = models.IntegerField("Kaina", null=False, help_text="Paslaugos kaina")

    def __str__(self):
        return f"{self.pavadinimas} {self.kaina}"


class Automobilis(models.Model):
    valstybinis_nr = models.CharField("Valstyvinis_NR", max_length=200, blank=True)
    automobilio_modelis = models.ForeignKey("Automobilio_modelis", on_delete=models.CASCADE, null=False)
    vin_kodas = models.CharField("VIN kodas", max_length=20, blank=True)
    klientas = models.CharField("Klientas", max_length=200, blank=True)

    def __str__(self):
        return f"{self.valstybinis_nr} {self.automobilio_modelis} {self.vin_kodas} {self.klientas}"


class Automobilio_modelis(models.Model):
    marke = models.CharField("Marke", max_length=200, blank=True)
    modelis = models.CharField("Modelis", max_length=200, blank=True)

    def __str__(self):
        return f"{self.marke} {self.modelis}"


class Uzsakymas(models.Model):
    data = models.DateField("Data", null=False)
    automobilis = models.ForeignKey("Automobilis", on_delete=models.SET_NULL, null=True)
    suma = models.IntegerField("Suma")

    def __str__(self):
        return f"{self.data} {self.automobilis}{self.suma}"


class Uzsakymu_eilute(models.Model):
    paslauga = models.ForeignKey("Paslauga", on_delete=models.SET_NULL, null=True)
    uzsakymai = models.ForeignKey("Uzsakymas", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis", null=False)
    kaina = models.IntegerField("Kaina", null=False)

    def __str__(self):
        return f"{self.paslauga} {self.uzsakymai} {self.kiekis} {self.kaina}"
