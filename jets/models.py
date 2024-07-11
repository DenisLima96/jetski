from django.db import models


class jet(models.Model):
    #Id do jet
    id = models.AutoField(primary_key=True)
    # Modelo do jetSki
    model = models.CharField(max_length=200)
    # Marca do JetSki
    brand = models.CharField(max_length=200)
    #Ano de Fabricação 
    factory_year = models.IntegerField(blank=True, null=True)
    #Ano do modelo do jet
    model_year = models.IntegerField(blank=True, null=True)
    # Valor que é em reais
    value = models.FloatField(blank=True, null=True)

    def __str__(self):
       return self.model
     
