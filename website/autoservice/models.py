from django.db import models


# Create your models here.
class Paslauga(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=200, help_text="Paslaugos pavadinimas")
    kaina = models.IntegerField("Kaina", help_text="Paslaugos kaina")

    def __str__(self):
        return f"{self.pavadinimas} {self.kaina}"


class Automobilis(models.Model):
    valstybinis_nr = models.CharField("Valstyvinis_NR", max_length=200)
    automobilio_modelis = models.ForeignKey("Automobilio_modelis", on_delete=models.CASCADE, null=False)
    vin_kodas = models.CharField("VIN kodas", max_length=20)
    klientas = models.CharField("Klientas", max_length=200)


    def __str__(self):
        return f"{self.valstybinis_nr} {self.automobilio_modelis} {self.vin_kodas} {self.klientas}"


class Automobilio_modelis(models.Model):
    marke = models.CharField("Marke", max_length=200)
    modelis = models.CharField("Modelis", max_length=200)

    def __str__(self):
        return f"{self.marke} {self.modelis}"

    class Meta:
        verbose_name ="Automobilis"
        verbose_name_plural ="Automobiliai"


class Uzsakymas(models.Model):
    data = models.DateField("Data", null=False)
    automobilis = models.ForeignKey("Automobilis", on_delete=models.SET_NULL, null=True)
    suma = models.IntegerField("Suma")

    def __str__(self):
        return f"{self.data} {self.automobilis}{self.suma}"

    class Meta:
        verbose_name = "Uzsakymas"
        verbose_name_plural = "Uzsakymai"

    LOAN_STATUS = (
        ('a', "Laukiama Apmokejimo"),
        ('p', "Vygdoma"),
        ('g', "On Hold"),
        ('r', "Ivygditas"),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default="a", help_text="Statusas")

class Uzsakymu_eilute(models.Model):
    paslauga = models.ForeignKey("Paslauga", on_delete=models.SET_NULL, null=True)
    uzsakymai = models.ForeignKey("Uzsakymas", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis", null=False)
    kaina = models.IntegerField("Kaina", null=False)

    def __str__(self):
        return f"{self.paslauga} {self.uzsakymai} {self.kiekis} {self.kaina}"
