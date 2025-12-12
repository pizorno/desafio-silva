import json
from django.core.management.base import BaseCommand
from core.models import Especie

class Command(BaseCommand):
    help = 'Importa espécies do arquivo species.json'

    def handle(self, *args, **kwargs):
        try:
            with open('species.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                
            for item in data:
                # Converte a lista de biomas em uma string única
                biomes_str = ", ".join(item['biomes'])
                
                Especie.objects.update_or_create(
                    id=item['id'],
                    defaults={
                        'common_name': item['commonName'],
                        'scientific_name': item['scientificName'],
                        'biomes': biomes_str,
                        'description': item['description']
                    }
                )
            self.stdout.write(self.style.SUCCESS(f'{len(data)} espécies importadas com sucesso!'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Arquivo species.json não encontrado na raiz.'))