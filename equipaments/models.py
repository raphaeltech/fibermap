from django.db import models


class boxs(models.Model):
    description = models.CharField(blank=False, null=True, max_length=256, verbose_name="Descrição")
    model = models.CharField(blank=False, null=True, max_length=256, verbose_name="Modelo")
    manufacturer = models.CharField(blank=False, null=True, max_length=256, verbose_name="Fabricante")
    price = models.FloatField(null=True, blank=True, verbose_name="Preço")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    update_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.description

class cables(models.Model):
    description = models.CharField(blank=False, null=True, max_length=256, verbose_name="Descrição")
    model = models.CharField(blank=False, null=True, max_length=256, verbose_name="Modelo")
    manufacturer = models.CharField(blank=False, null=True, max_length=256, verbose_name="Fabricante")
    priceForMetter = models.FloatField(null=True, blank=True, verbose_name="Preço")
    type = models.CharField(blank=False, null=True, max_length=256, verbose_name="Tipo")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    update_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.description

class steels(models.Model):
    description = models.CharField(blank=False, null=True, max_length=256, verbose_name="Descrição")
    model = models.CharField(blank=False, null=True, max_length=256, verbose_name="Modelo")
    manufacturer = models.CharField(blank=False, null=True, max_length=256, verbose_name="Fabricante")
    price = models.FloatField(null=True, blank=True, verbose_name="Preço")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    update_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.description

class poles(models.Model):
    type = models.CharField(null=True, blank=False, max_length=256, verbose_name="Tipo")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    update_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.type

class spliters(models.Model):
    description = models.CharField(null=True, blank=False, max_length=256, verbose_name="Descrição")
    model = models.CharField(null=True, blank=False, max_length=256, verbose_name="Modelo")
    manufacturer = models.CharField(blank=False, null=True, max_length=256, verbose_name="Fabricante")
    type = models.CharField(null=True, blank=False, max_length=256, verbose_name="Tipo")
    price = models.FloatField(null=True, blank=True, verbose_name="Preço")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    update_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.description

# Create your models here.
