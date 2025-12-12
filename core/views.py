from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Especie
from django import forms

# Form para usar no Create e Update com classes Bootstrap
class EspecieForm(forms.ModelForm):
    class Meta:
        model = Especie
        fields = ['common_name', 'scientific_name', 'biomes', 'description']
        widgets = {
            'common_name': forms.TextInput(attrs={'class': 'form-control'}),
            'scientific_name': forms.TextInput(attrs={'class': 'form-control'}),
            'biomes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Cerrado, Amazônia'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class EspecieListView(ListView):
    model = Especie
    template_name = 'core/especie_list.html'
    context_object_name = 'especies'
    paginate_by = 12  # Paginação: 12 cards por página

    def get_queryset(self):
        queryset = super().get_queryset()
        termo_busca = self.request.GET.get('q')
        
        if termo_busca:
            # Busca em nome comum, científico OU biomas
            queryset = queryset.filter(
                Q(common_name__icontains=termo_busca) |
                Q(scientific_name__icontains=termo_busca) |
                Q(biomes__icontains=termo_busca)
            )
        return queryset

class EspecieCreateView(CreateView):
    model = Especie
    form_class = EspecieForm
    template_name = 'core/especie_form.html'
    success_url = reverse_lazy('especie_list')
    extra_context = {'titulo': 'Nova Espécie'}

class EspecieUpdateView(UpdateView):
    model = Especie
    form_class = EspecieForm
    template_name = 'core/especie_form.html'
    success_url = reverse_lazy('especie_list')
    extra_context = {'titulo': 'Editar Espécie'}