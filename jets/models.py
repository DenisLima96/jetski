from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        


class jet(models.Model):
    #Id do jet
    id = models.AutoField(primary_key=True)
    # Modelo do jetSki
    model = models.CharField(max_length=200)
    # Marca do JetSki
    brand = models.ForeignKey(Brand, on_delete=models. PROTECT, related_name='jet_brand')
    #Ano de Fabricação 
    factory_year = models.IntegerField(blank=True, null=True)
    #Ano do modelo do jet
    model_year = models.IntegerField(blank=True, null=True)
    #chassi  da embarcação 
    plate = models.CharField(max_length=10, blank=True, null=True)
    # Valor que é em reais
    value = models.FloatField(blank=True, null=True)
    #campo de imagem
    photo =models.ImageField(upload_to='jets/', blank=True, null=True)


    def __str__(self):
       return self.model
     
