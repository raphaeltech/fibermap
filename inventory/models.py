from django.db import models
from django_google_maps import fields as map_fields

class ctos(models.Model):
    identification = models.CharField(max_length=256,null=False, blank=False, verbose_name="Identificação")
    ctoModel = models.ForeignKey ("equipaments.boxs", on_delete=models.CASCADE, default=1, verbose_name="Modelo da CTO")
    pole = models.ForeignKey("positionPoles", on_delete=models.CASCADE, default=1, verbose_name="Poste")
    spliter1 = models.ForeignKey("equipaments.spliters", on_delete=models.CASCADE, default=1, null=True, blank=True, related_name="spliter1", verbose_name="Spliter 1")
    spliter2 = models.ForeignKey("equipaments.spliters", on_delete=models.CASCADE, default=1, null=True, blank=True, related_name='spliter2', verbose_name="Spliter 2")
    spliter3 = models.ForeignKey("equipaments.spliters", on_delete=models.CASCADE, default=1, null=True, blank=True, related_name='spliter3', verbose_name="Spliter 3")
    fusion = models.BooleanField(null=True, verbose_name="Existe Fusão?")
    numberFusion = models.BigIntegerField(null=True, blank=True, verbose_name="Numero de fusões")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    update_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.identification

class ceos(models.Model):
    identification = models.CharField(max_length=256,null=False, blank=False, verbose_name="Identificação")
    ceoModel = models.ForeignKey ("equipaments.boxs", on_delete=models.CASCADE, default=1, verbose_name="Modelo da CEO")
    pole = models.ForeignKey("positionPoles", on_delete=models.CASCADE, default=1, verbose_name="Poste")
    numberTray = models.BigIntegerField(null=True, verbose_name="Numero de Bandeijas")
    numberFusion = models.BigIntegerField(null=True, verbose_name="Numero de Fusões")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    update_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.identification

class positionPoles(models.Model):
    
    identification = models.CharField(max_length=256,null=False, blank=False, verbose_name="Identificação")
    geolocation = map_fields.GeoLocationField(max_length=100)
    poleModel = models.ForeignKey("equipaments.poles", on_delete=models.CASCADE, default=1, verbose_name="Modelo do Poste")
    isLocate = models.BooleanField(null=True, blank=True, verbose_name='Alugado')
    priceLocation = models.FloatField(null=True, blank=True, verbose_name="Valor da locação")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    update_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.identification

class positionSteels(models.Model):
    identification = models.CharField(max_length=256,null=False, blank=False, verbose_name="Identificação")
    modelSteel = models.ForeignKey("equipaments.steels", on_delete=models.CASCADE, default=1, verbose_name="Modelo da Ferragem")
    poleIdentification = models.ForeignKey("positionPoles", on_delete=models.CASCADE, default=1, verbose_name="Poste")
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    update_at = models.DateTimeField(auto_now=True, blank=False, null=True)

    def __str__(self):
        return self.identification



# Class refereces for views mysqls
    
class ceoprices(models.Model):
    ceoModel_id = models.IntegerField()
    description = models.CharField(max_length=256)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ceoPrices'

class ctoprices(models.Model):
    ctoModel_id = models.IntegerField()
    description = models.CharField(max_length=256)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ctoPrices'

class polepriceslocation(models.Model):
    identification = models.IntegerField()
    geolocation = models.CharField(max_length=256)
    isLocate = models.BooleanField()
    priceLocation = models.FloatField()

    class Meta:
        managed = False
        db_table = 'polePricesLocation'

class spliterprices(models.Model):
    spliter1_id = models.IntegerField()
    spliter2_id = models.IntegerField()
    spliter3_id = models.IntegerField()
    description = models.CharField(max_length=256)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'spliterPrices'

class steelprices(models.Model):
    modelSteel_id = models.IntegerField()
    description = models.CharField(max_length=256)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'steelPrices'