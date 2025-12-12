from django.contrib import admin
from django.urls import path
from core.views import EspecieListView, EspecieCreateView, EspecieUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EspecieListView.as_view(), name='especie_list'),
    path('adicionar/', EspecieCreateView.as_view(), name='especie_create'),
    path('editar/<int:pk>/', EspecieUpdateView.as_view(), name='especie_update'),
]