from django.db import models

class Especie(models.Model):
    common_name = models.CharField("Nome Comum", max_length=200)
    scientific_name = models.CharField("Nome Científico", max_length=200)
    # Vamos armazenar biomas como texto separado por vírgula para facilitar a busca simples
    biomes = models.CharField("Biomas", max_length=255) 
    description = models.TextField("Descrição")

    def __str__(self):
        return self.common_name
    
    @property
    def lista_biomas(self):
        """Retorna os biomas como uma lista limpa, removendo espaços extras"""
        if self.biomes:
            # Divide pela vírgula e remove espaços em branco de cada item
            return [b.strip() for b in self.biomes.split(',')]
        return []

    class Meta:
        ordering = ['common_name']